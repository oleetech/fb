from django import forms
from .models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput,label='')

    class Meta:
        model = User
        fields = ('email', 'password')
        labels = {
            'email': '',
            
        }
