from django import forms
from django.contrib.auth.forms import UserCreationForm

from users.models import User


class SignupForm(UserCreationForm):
    """ Cette class sert à enregistrer username, ces 2 password et l'email """

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")