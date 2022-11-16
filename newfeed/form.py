
from operator import attrgetter
from tkinter import Widget
from unicodedata import name
from django import forms
from .models import Post_content, Comment
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    content = forms.CharField(
        required=True,
        widget=forms.widgets.Textarea(
            attrs={
                "placeholder": "write something...",
                "rows": "2",
            }
        )
    )
    image = forms.ImageField(
        required=False,
        widget=forms.widgets.FileInput(
            attrs={
                "class": "fa fa-image"
            }
        )
    )
    
    
    class Meta:
        model = Post_content
        fields = ('content','image',)
        
class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user_name = kwargs.pop('user_name', None)
        self.post = kwargs.pop('post', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        comment = super().save(commit=False)
        comment.user_name = self.user_name
        comment.post = self.post
        comment.save()
    class Meta:
        model = Comment
        fields = ["user_comment", "image_comment"]
    
    

