from django import forms
from django.forms import Textarea
from .models import Post, Comment


class PostCreationForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].widget = Textarea(attrs={'rows': 3})
        # self.fields['content'].text = ''
