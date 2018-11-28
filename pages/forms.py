from django import forms
from django.forms import ModelForm, HiddenInput
from .models import Boards


class BoardForm(ModelForm):

    class Meta:
        model = Boards
        fields = '__all__'
        widgets = {'boardr': HiddenInput(),
                   'boardg': HiddenInput(),
                   'boardb': HiddenInput(),
                   'boardtiltx': HiddenInput(),
                   'boardtilty': HiddenInput(),
                   'boardbackgroundr': HiddenInput(),
                   'boardbackgroundg': HiddenInput(),
                   'boardbackgroundb': HiddenInput(),
                   }
