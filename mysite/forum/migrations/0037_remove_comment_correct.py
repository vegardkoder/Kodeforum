# Generated by Django 2.0.3 on 2018-08-06 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0036_auto_20180806_1022'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='correct',
        ),
    ]
