# Generated by Django 2.1.7 on 2019-04-08 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jmiforums', '0002_profile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aritcles',
            name='subforum_id',
        ),
        migrations.RemoveField(
            model_name='aritcles',
            name='user_id',
        ),
        migrations.DeleteModel(
            name='Aritcles',
        ),
    ]