from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext as _
from django import forms

from system.users.models import User


class UserForm(UserCreationForm):
    username = forms.CharField(
        help_text=_("Letter, digits and @/./+/-/_ only"),
        max_length=150,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control'
        })
    )

    password1 = forms.CharField(
        help_text=_("""Your password must contain at least
            8 characters and can't be entirely numeric."""),
        widget=forms.PasswordInput(attrs={
            'class': 'form-control'
        }),
        max_length=150,
        required=False,
    )

    password2 = forms.CharField(
        help_text=_("Enter the same password as above, for verification."),
        widget=forms.PasswordInput(attrs={
            'class': 'form-control'
        }),
        max_length=150,
        required=False,
    )

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
