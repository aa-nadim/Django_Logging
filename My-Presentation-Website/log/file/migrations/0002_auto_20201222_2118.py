# Generated by Django 3.1.4 on 2020-12-22 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eventsform',
            old_name='email',
            new_name='error_type',
        ),
        migrations.RenameField(
            model_name='eventsform',
            old_name='name',
            new_name='message',
        ),
        migrations.RenameField(
            model_name='eventsform',
            old_name='phone',
            new_name='time',
        ),
    ]
