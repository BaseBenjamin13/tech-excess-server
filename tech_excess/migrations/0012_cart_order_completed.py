# Generated by Django 4.0.6 on 2022-07-17 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tech_excess', '0011_rename_user_cart_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='order_completed',
            field=models.BooleanField(default=False),
        ),
    ]