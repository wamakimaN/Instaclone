from django import forms
from .models import  Post, Profile

class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ['image','caption','profile']

class ProfileUpdateForm(forms.ModelForm):
  class Meta:
    model = Profile
    fields = []