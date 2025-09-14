from django import forms
from django.forms import inlineformset_factory
from .models import Vibe, VibeMedia


class VibeForm(forms.ModelForm):
  class Meta:
      model = Vibe
      fields = ['text']


class VibeMediaForm(forms.ModelForm):
  class Meta:
      model = VibeMedia
      fields = ['file']


# Inline formset: links Vibe ↔ VibeMedia
VibeMediaFormSet = inlineformset_factory(
  Vibe, VibeMedia,
  form=VibeMediaForm,
  fields=['file'],
  extra=1,     # how many empty slots to show initially
  max_num=5,   # limit to 5 files
  can_delete=True
)