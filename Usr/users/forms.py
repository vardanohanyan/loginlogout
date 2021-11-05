from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(help_text=False)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email']





class NameForm(forms.Form):
    your_name = forms.CharField(label='your_name', max_length=100)


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

class ContactUs(forms.Form):
    first_name = forms.CharField(max_length=40)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField(required=True)
    massage = forms.CharField(widget=forms.Textarea, max_length=500)

