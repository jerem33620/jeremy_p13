from django import forms
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from PIL import Image

from users.models import User


class SignupForm(UserCreationForm):
    """ Cette class sert à enregistrer username, ces 2 password et l'email """

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")


class AvatarChangeForm(forms.Form):
    avatar = forms.FileField(required=False)
    x = forms.FloatField(widget=forms.HiddenInput())
    y = forms.FloatField(widget=forms.HiddenInput())
    width = forms.FloatField(widget=forms.HiddenInput())
    height = forms.FloatField(widget=forms.HiddenInput())

    def save(self, request):
        user = request.user
        user.avatar = request.FILES['avatar']
        user.save()

        x = self.cleaned_data.get('x')
        y = self.cleaned_data.get('y')
        width = self.cleaned_data.get('width')
        height = self.cleaned_data.get('height')

        avatar = Image.open(user.avatar)
        cropped_avatar = avatar.crop((x, y, x + width, y + height))
        resized_avatar = cropped_avatar.resize(
            settings.USER_AVATAR_SIZE, Image.ANTIALIAS
        )
        resized_avatar.save(user.avatar.path)

        return avatar
