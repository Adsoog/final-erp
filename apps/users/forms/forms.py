from django import forms
from django.contrib.auth.forms import AuthenticationForm

from apps.users.models.user import User


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Username',
    )

    password = forms.CharField(label='Password')

    class Meta:
        model = User
        fields = ['username', 'password']
