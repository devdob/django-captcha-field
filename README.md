# Django Captcha field (In Progress)

Google Captcha V3 integrated form field

# Installation

PIP:
`pip install django-captcha3`

GIT:
`git clone https://github.com/sitmena/django-captcha-field`

# Usage

Add the package `captcha_field` to your installed apps. Then you can simply add
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


