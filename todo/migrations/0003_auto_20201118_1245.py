# Generated by Django 2.2.16 on 2020-11-18 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20190321_2306'),
    ]

    operations = [
        migrations.AddField(
            model_name='todomodel',
            name='radius',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='todomodel',
            name='x',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='todomodel',
            name='y',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='todomodel',
            name='title',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
