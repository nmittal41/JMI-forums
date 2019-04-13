# Generated by Django 2.1.7 on 2019-04-12 07:14

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jmiforums', '0004_auto_20190409_0457'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='upvote',
        ),
        migrations.AddField(
            model_name='answer',
            name='upvote',
            field=models.ManyToManyField(blank=True, related_name='ans_upvote', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='question',
            name='upvote',
        ),
        migrations.AddField(
            model_name='question',
            name='upvote',
            field=models.ManyToManyField(blank=True, related_name='ques_upvote', to=settings.AUTH_USER_MODEL),
        ),
    ]