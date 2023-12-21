from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'body']
        widgets = {
            'body': forms.Textarea(attrs={'rows': 500}),  # Adjust the number of rows as needed
        }