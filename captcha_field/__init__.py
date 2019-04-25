import requests

from django.forms import Field

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
        super().__init__()  # Call main init first
        self.widget.input_type = 'hidden'
        self.widget.template_name = 'captcha_field.html'
        if 'widget' in kwargs and kwargs['widget'].attrs:
            self.widget.attrs['google_captcha_key'] = kwargs['widget'].attrs['google_captcha_key']
            self.widget.attrs['google_captcha_secret'] = kwargs['widget'].attrs['google_captcha_secret']

    def validate(self, value):
        pass
        # super().validate()
        # res = requests.post('https://www.google.com/recaptcha/api/siteverify',
        #                     data={
        #                         'secret': '6LelsJwUAAAAAOChZy-v5OYqJfXN0u84vfAfJvk5',
        #                         'response': request.POST[
        #                             'g-recaptcha-response']})
        # if 'success' in res and res['success'] and res['score'] > 0.5:
        #     send_mail = True
