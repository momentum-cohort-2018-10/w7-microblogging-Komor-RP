# Generated by Django 2.1.4 on 2018-12-16 01:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_auto_20181216_0125'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='follow',
        ),
    ]
