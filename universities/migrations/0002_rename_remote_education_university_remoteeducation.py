# Generated by Django 4.2 on 2024-03-21 11:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('universities', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='university',
            old_name='remote_education',
            new_name='remoteEducation',
        ),
    ]
