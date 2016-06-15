from django import forms

class PostComment(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)
