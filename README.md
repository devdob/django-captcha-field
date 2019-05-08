# Django google Captcha V3 field

Google Captcha V3 integrated form field

# Installation

GIT:

`pip install git+https://github.com/sitmena/django-captcha-field@v1.0`

# Usage

Add the package `django-captcha3` to your installed apps. Then you can simply add
to your form like so,

```python
from captcha_field import CaptchaField


class MyForm(forms.Form):
    my_field_1 = forms.CharField(required=True, label='')
    ...
    captcha = CaptchaField(google_captcha_key='my_key',
                           google_captcha_secret='my_secret')

```

# Testing


