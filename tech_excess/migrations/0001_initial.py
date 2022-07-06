# Generated by Django 4.0.5 on 2022-07-05 23:53

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='no title', max_length=50)),
                ('brand', models.CharField(default='brand not found', max_length=20)),
                ('category', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('on_sale', models.BooleanField(default=False)),
                ('featured_image_url', models.CharField(default='No image', max_length=500)),
                ('image_urls', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(default='No image', max_length=500), max_length=5, size=None)),
            ],
        ),
        migrations.CreateModel(
            name='ItemReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(default='unknown', max_length=50)),
                ('body', models.TextField()),
                ('rating', models.IntegerField()),
                ('monitor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='tech_excess.item')),
            ],
        ),
    ]
