from django import forms
from django.forms import inlineformset_factory
from .models import Vibe

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class VibeForm(forms.ModelForm):
  class Meta:
      model = Vibe
      fields = ['text', 'media']

class UserRegistrationForm(UserCreationForm):
  email = forms.EmailField()
  class Meta :
    model = User
    fields = ('username', 'email', 'password1', 'password2')
