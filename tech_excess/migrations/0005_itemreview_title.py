# Generated by Django 4.0.6 on 2022-07-11 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tech_excess', '0004_remove_itemreview_owner_alter_itemreview_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemreview',
            name='title',
            field=models.CharField(default='Title here', max_length=100),
        ),
    ]