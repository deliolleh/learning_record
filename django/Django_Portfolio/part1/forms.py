from django import forms
from .models import Liquor, Comment


class LiquorForm(forms.ModelForm):

    class Meta:
        model = Liquor
        exclude = ('user', )


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('content',)
