# Generated by Django 2.0.3 on 2018-07-12 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0006_auto_20180711_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, default='profile_image/userpicture2', upload_to='profile_image'),
        ),
    ]
