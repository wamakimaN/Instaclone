from django import forms
from .models import  Post, Profile

class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    exclude = ['profile','posted_on']

class ProfileUpdateForm(forms.ModelForm):
  class Meta:
    model = Profile
    fields = []