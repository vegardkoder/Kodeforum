# Generated by Django 2.0.3 on 2018-05-08 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0006_remove_post_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(default=1, on_delete=None, related_name='comment', to='forum.Post'),
            preserve_default=False,
        ),
    ]
