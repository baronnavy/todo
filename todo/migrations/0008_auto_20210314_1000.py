# Generated by Django 2.2.17 on 2021-03-14 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0007_auto_20210314_0945'),
    ]

    operations = [
        migrations.AddField(
            model_name='todomodel',
            name='article',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='todomodel',
            name='company',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='todomodel',
            name='end',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='todomodel',
            name='floor',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='todomodel',
            name='start',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
