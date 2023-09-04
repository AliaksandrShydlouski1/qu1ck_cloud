from django import forms
from django.forms import ModelForm, TextInput, FileInput, DateInput, NumberInput, ClearableFileInput
from .models import cloud
from django.db import models

class IdentForm(forms.Form):
    ident = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'code21', 'placeholder': '123456'}),
        max_value = 999999
    )
class CloudForm(ModelForm):
    class Meta:
        model = cloud
        fields = ['title', 'text', 'file', 'ident', 'image']
        widgets = {
            "title": TextInput(attrs={'class':'form-control', 'placeholder':'Title'}),
            "text": TextInput(attrs={ 'class':'form-control', 'placeholder': 'Text'}),
            "file": FileInput(attrs={'class': 'form-control', 'id': "inputGroupFile02"}),
            'image': FileInput(attrs={'class': 'form-control', 'id': "inputGroupFile02"}),
            "ident": NumberInput()

            #"date": DateInput(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['ident'].required = False
        self.fields['file'].required = False
        self.fields['image'].required = False
        self.fields['text'].required = False

