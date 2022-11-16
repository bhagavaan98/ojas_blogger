from django.contrib.auth.models import User
from django import forms
from .models import Contact,blog
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    password2=forms.CharField(label="Confirm password (again)",widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        
class ContactForm(forms.Form):
    first_name=forms.CharField()
    last_name=forms.CharField()
    options=(('1',"india"),('2',"america"),('3',"chaina"))
    country=forms.ChoiceField(choices=options)
    mobile_no=forms.IntegerField()
    email=forms.EmailField()
    address=forms.CharField(widget=forms.Textarea)


class blogForm(forms.ModelForm):
    class Meta:
        model=blog
        fields="__all__"

