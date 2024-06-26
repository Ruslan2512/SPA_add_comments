# Generated by Django 5.0.6 on 2024-06-16 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("comments", "0003_remove_comment_file"),
    ]

    operations = [
        migrations.RemoveField(model_name="comment", name="image",),
        migrations.AddField(
            model_name="comment",
            name="avatar",
            field=models.ImageField(blank=True, null=True, upload_to="avatars/"),
        ),
        migrations.AlterField(
            model_name="comment",
            name="username",
            field=models.CharField(max_length=100),
        ),
    ]
