# Generated by Django 3.1.5 on 2021-02-19 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0005_listing_lot_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='beds',
            field=models.CharField(default='', max_length=10),
        ),
    ]
