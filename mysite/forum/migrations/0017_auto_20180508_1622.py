# Generated by Django 2.0.3 on 2018-05-08 14:22

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0016_auto_20180508_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.OneToOneField(on_delete=None, to=settings.AUTH_USER_MODEL),
        ),
    ]
