# Generated by Django 2.1 on 2018-11-23 19:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0003_attendance'),
    ]

    operations = [
        migrations.RenameField(
            model_name='students',
            old_name='unit_name',
            new_name='unit',
        ),
    ]
