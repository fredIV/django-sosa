from django import forms
from pages import models
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email', 'username',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'username',)

# class PostBoard(forms.ModelForm):
#
#     class Meta:
#         model = models.board
#         fields = ('boardR', 'boardB', 'boardG', 'backgroundR', 'backgroundG', 'backgroundB', 'board_tilt_x',
#           'board_tilt_y', 'admin_ID')
