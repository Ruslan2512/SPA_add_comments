from django import forms
from .models import Comment
from captcha.fields import CaptchaField


class CommentForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:  # Вказування моделі на якій базується форма
        model = Comment
        fields = ['username', 'email', 'text', 'image', 'text_file', 'parent']  # Поля які включені до форми
