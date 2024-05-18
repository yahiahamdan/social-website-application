from django import forms
from django.contrib.auth.models import User
"""
we zey ma olna deh wedgiet 
widget bt5lehaa lma t3mlha render   browser treat as passwo input
"""
class loginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(forms.ModelForm):
    password=forms.CharField(label='Password',widget=forms.PasswordInput)
    password2=forms.CharField(label='Repeat Password',widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=('username','first_name','email')
    def clean_password2(self):
        cd=self.cleaned_data
        if cd['password']!=cd['password2']:
            raise forms.ValidationError('passwords dont match')
        return cd['password2']