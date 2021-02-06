import io

from django import forms
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.core.files.uploadedfile import SimpleUploadedFile
from PIL import Image

from users.models import User


class SignupForm(UserCreationForm):
    """ Cette class sert à enregistrer username, ces 2 password et l'email """

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")


class AvatarChangeForm(forms.Form):
    avatar = forms.FileField(required=False)
    x = forms.FloatField(required=False, widget=forms.HiddenInput())
    y = forms.FloatField(required=False, widget=forms.HiddenInput())
    width = forms.FloatField(required=False, widget=forms.HiddenInput())
    height = forms.FloatField(required=False, widget=forms.HiddenInput())

    def save(self, request, commit=True):
        user = request.user

        if self.cleaned_data.get('avatar'):
            avatar = self.cleaned_data.get('avatar')
            x = self.cleaned_data.get('x')
            y = self.cleaned_data.get('y')
            width = self.cleaned_data.get('width')
            height = self.cleaned_data.get('height')

            if x is not None:
                avatar_img = Image.open(io.BytesIO(avatar.read()))
                cropped_avatar = avatar_img.crop((x, y, x + width, y + height))
                resized_avatar = cropped_avatar.resize(
                    settings.USER_AVATAR_SIZE, Image.ANTIALIAS
                )
                buffer = io.BytesIO()
                resized_avatar.save(buffer, format=avatar_img.format)
                avatar = SimpleUploadedFile(
                    avatar.name, buffer.getvalue(), avatar.content_type
                )
            user.avatar = avatar
            if commit:
                user.save()

        return user
