from django import forms
from .models import Comment
from captcha.fields import CaptchaField


class CommentForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Comment
        fields = ['username', 'email', 'text', 'image', 'text_file', 'parent']

