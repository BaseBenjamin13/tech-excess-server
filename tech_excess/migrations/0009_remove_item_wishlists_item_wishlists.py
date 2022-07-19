# Generated by Django 4.0.6 on 2022-07-14 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tech_excess', '0008_alter_wishlist_options_remove_wishlist_items_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='wishlists',
        ),
        migrations.AddField(
            model_name='item',
            name='wishlists',
            field=models.ManyToManyField(related_name='items', to='tech_excess.wishlist'),
        ),
    ]