# Generated by Django 2.2.7 on 2019-11-19 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippet', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Snippets',
            new_name='Snippet',
        ),
    ]
