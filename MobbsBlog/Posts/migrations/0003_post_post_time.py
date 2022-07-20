# Generated by Django 3.2.14 on 2022-07-20 19:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0002_post_post_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_time',
            field=models.TimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]