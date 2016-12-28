from django import forms
from .models import blogEntry

class BlogForm(forms.ModelForm):

    class Meta:
        model = blogEntry
        fields = ["name", "description", "tags"]