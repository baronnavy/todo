# Generated by Django 2.2.17 on 2021-03-30 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0010_auto_20210319_0009'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reserve',
            old_name='article2',
            new_name='article',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='reserve',
        ),
    ]