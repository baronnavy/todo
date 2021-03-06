# Generated by Django 2.2.17 on 2021-03-13 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_reservation'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='floor',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='article',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='company',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='end',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='start',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
