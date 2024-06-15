from django.db import models


class Comment(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField()
    home_page = models.URLField(blank=True, null=True)
    captcha = models.CharField(max_length=255)
    text = models.TextField()
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
