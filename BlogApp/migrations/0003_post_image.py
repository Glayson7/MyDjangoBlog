# Generated by Django 4.2.6 on 2023-10-19 20:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "BlogApp",
            "0002_remove_post_image_alter_comment_user_alter_like_user_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="post_images/"),
        ),
    ]
