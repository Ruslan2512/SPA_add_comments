# Generated by Django 5.0.6 on 2024-06-16 09:18

import comments.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("comments", "0004_remove_comment_image_comment_avatar_and_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="comment", name="avatar",),
        migrations.AddField(
            model_name="comment",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="images/"),
        ),
        migrations.AddField(
            model_name="comment",
            name="text_file",
            field=models.FileField(
                blank=True,
                null=True,
                upload_to="text_files/",
                validators=[comments.models.validate_file_size],
            ),
        ),
    ]
