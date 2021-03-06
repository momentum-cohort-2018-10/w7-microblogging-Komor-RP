# Generated by Django 2.1.4 on 2018-12-11 19:42

from django.db import migrations, models
import posts.validation


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_poster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(max_length=280, validators=[posts.validation.min_post_length]),
        ),
    ]
