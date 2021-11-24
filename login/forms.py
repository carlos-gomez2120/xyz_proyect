from builtins import super

from django.contrib.auth.forms import AuthenticationForm

class formulario_login(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(formulario_login, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'USER'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'PASSWORD'