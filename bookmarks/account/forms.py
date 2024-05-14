from django import forms
"""
we zey ma olna deh wedgiet 
widget bt5lehaa lma t3mlha render   browser treat as passwo input
"""
class loginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)
