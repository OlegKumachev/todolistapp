# Generated by Django 5.1.4 on 2024-12-23 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tasks',
            old_name='descriotion',
            new_name='description',
        ),
    ]