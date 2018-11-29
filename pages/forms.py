from django import forms
from django.forms import ModelForm, HiddenInput
from .models import *


class BoardForm(ModelForm):
    class Meta:
        model = Boards
        fields = '__all__'
        widgets = {'user': HiddenInput(),
                   'boardr': HiddenInput(),
                   'boardg': HiddenInput(),
                   'boardb': HiddenInput(),
                   'boardtiltx': HiddenInput(),
                   'boardtilty': HiddenInput(),
                   'boardbackgroundr': HiddenInput(),
                   'boardbackgroundg': HiddenInput(),
                   'boardbackgroundb': HiddenInput(),
                   }


class BoardEditForm(ModelForm):
    class Meta:
        model = Boards
        fields = ['boardname',
                  'boardr',
                  'boardg',
                  'boardb',
                  'boardtiltx',
                  'boardtilty',
                  'boardbackgroundr',
                  'boardbackgroundg',
                  'boardbackgroundb',
                  ]
        widgets = {'boardr': HiddenInput(),
                   'boardg': HiddenInput(),
                   'boardb': HiddenInput(),
                   'boardtiltx': HiddenInput(),
                   'boardtilty': HiddenInput(),
                   'boardbackgroundr': HiddenInput(),
                   'boardbackgroundg': HiddenInput(),
                   'boardbackgroundb': HiddenInput(),
                   }


class StimSetForm(ModelForm):
    class Meta:
        model = StimSets
        fields = "__all__"
        widgets = {'user': HiddenInput()}


class StimForm(ModelForm):
    class Meta:
        model = Stims
        fields = '__all__'
        widgets = {'stimsetid': HiddenInput(),
                   'stimr': HiddenInput(),
                   'stimg': HiddenInput(),
                   'stimb': HiddenInput(),
                   'labelr': HiddenInput(),
                   'labelg': HiddenInput(),
                   'labelb': HiddenInput(),
                   'stimshape': HiddenInput(),
                   }
