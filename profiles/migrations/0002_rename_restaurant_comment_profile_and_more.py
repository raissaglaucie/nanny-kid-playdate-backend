# Generated by Django 4.0.3 on 2023-07-07 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='restaurant',
            new_name='profile',
        ),
        migrations.RenameField(
            model_name='notification',
            old_name='blog',
            new_name='place',
        ),
    ]
