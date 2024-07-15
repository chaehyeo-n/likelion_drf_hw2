# Generated by Django 5.0.7 on 2024-07-15 16:04

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='like_user',
            field=models.ManyToManyField(blank=True, null=True, related_name='like_post', to=settings.AUTH_USER_MODEL),
        ),
    ]