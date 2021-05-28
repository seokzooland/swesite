from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    job = forms.CharField(label="직업")

    class Meta:
        model = User
        fields = ("username", "job")

