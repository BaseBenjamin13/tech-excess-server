# Generated by Django 4.0.6 on 2022-07-14 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tech_excess', '0006_wishlist'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='wishlist',
            options={'ordering': ['name']},
        ),
    ]
