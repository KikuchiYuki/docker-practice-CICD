# Generated by Django 4.2 on 2024-06-11 02:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mytodo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='complite',
            new_name='complete',
        ),
    ]