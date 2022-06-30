# Generated by Django 4.0.5 on 2022-06-30 01:51

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Monitors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='no title', max_length=50)),
                ('brand', models.CharField(default='brand not found', max_length=20)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('on_sale', models.BooleanField(default=False)),
                ('featured_image_url', models.CharField(default='No image', max_length=500)),
                ('image_urls', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(default='No image', max_length=500), max_length=5, size=None)),
            ],
        ),
    ]
