from django import forms
from .models import News, Comment

class PostForm(forms.ModelForm):

    class Meta:
        model = News
        fields = ('title', 'text',)
        
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)
