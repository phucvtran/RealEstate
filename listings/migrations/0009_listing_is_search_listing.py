# Generated by Django 3.1.5 on 2021-03-01 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0008_auto_20210218_2232'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='is_search_listing',
            field=models.BooleanField(default=False),
        ),
    ]