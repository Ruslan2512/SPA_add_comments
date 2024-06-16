from django.db import models
from django.core.exceptions import ValidationError

ALLOWED_HTML_TAGS = ['a', 'code', 'i', 'strong']


def validate_file_size(value):
    limit = 1024 * 100  # 100 KB
    if value.size > limit:
        raise ValidationError('File too large. Size should not exceed 100 KB.')


class Comment(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    text_file = models.FileField(upload_to='text_files/', null=True, blank=True, validators=[validate_file_size])

    def __str__(self):
        return self.email
