from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Comment(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField()
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='comment_images/', null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.image:
            img = Image.open(self.image)
            if img.height > 240 or img.width > 320:
                output_size = (320, 240)
                img.thumbnail(output_size)
                img.save(self.image.path)
        super().save(*args, **kwargs)
