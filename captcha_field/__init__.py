import requests
from django.core.exceptions import ValidationError

from django.forms import Field
from django.conf import settings

name = "captcha_field"


class CaptchaField(Field):
    """
    Base field class
    """

    def __init__(self, **kwargs):
        """
        Initilize field
        :param kwargs:
        """
        super().__init__()  # Call Field init first
        self.widget.input_type = 'hidden'
        self.widget.template_name = 'captcha-field.html'
        if 'widget' in kwargs and kwargs['widget'].attrs:
            self.widget.attrs['google_captcha_key'] = kwargs['widget'].attrs['google_captcha_key']
            self.widget.attrs['google_captcha_secret'] = kwargs['widget'].attrs['google_captcha_secret']
        elif 'google_captcha_key' in kwargs and 'google_captcha_secret' in kwargs:
            self.widget.attrs['google_captcha_key'] = kwargs['google_captcha_key']
            self.widget.attrs['google_captcha_secret'] = kwargs['google_captcha_secret']

    def validate(self, value):
        """
        Custom validate for captcha
        Raise validation error if success not in response or if success
        was None or if the score is less than 0.5
        :param value: field value
        :return:
        """
        try:
            r_limit = settings.GOOGLE_CAPTCHA_MIN_SCORE
        except:
            r_limit = 0.5
        res = requests.post('https://www.google.com/recaptcha/api/siteverify',
                            data={
                                'secret': self.widget.attrs['google_captcha_secret'],
                                'response': value}).json()
        if 'success' not in res or not res['success'] or res['score'] < r_limit:
            raise ValidationError('Captcha Validation Failed!')
