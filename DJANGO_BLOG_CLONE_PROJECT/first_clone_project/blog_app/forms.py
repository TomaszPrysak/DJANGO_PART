from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ('author', 'title', 'text')

        # Widgety są potrzebne jeżeli chcemy stylizować za pomocą CSS formularz atumatycznie wygenerowany przez model formularza django
        widget = {
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
        }

class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields = ('author', 'text')

        # Widgety są potrzebne jeżeli chcemy stylizować za pomocą CSS formularz atumatycznie wygenerowany przez model formularza django
        widget = {
            'author':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'})
        }
