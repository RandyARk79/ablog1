# Generated by Django 3.1 on 2020-10-07 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0004_post_post_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='update_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
