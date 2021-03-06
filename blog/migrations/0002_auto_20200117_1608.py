# Generated by Django 2.2.4 on 2020-01-18 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogentry',
            name='pub_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='blogentry',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, unique=True),
        ),
    ]
