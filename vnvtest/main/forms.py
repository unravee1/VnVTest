from .models import User, Group
from django import forms
from django.forms import ModelForm, TextInput, DateField, ModelChoiceField, Textarea, Select


class UserForm(ModelForm):
    username = forms.CharField( max_length=255)
    group = forms.ModelChoiceField(queryset=Group.objects.all(), )
    class Meta:
        model = User
        fields = ['username','group']
        widgets = {
          "username": TextInput(attrs={
              'class': 'form-control',
               'placeholder': 'Enter username'
           }),
            "group": Select(attrs={
                'class': 'form-control',

            }),
     }


class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'description']
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter name'
            }),
            "description": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter description'
            }),
        }
