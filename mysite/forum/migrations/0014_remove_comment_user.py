# Generated by Django 2.0.3 on 2018-05-08 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0013_comment_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
    ]
