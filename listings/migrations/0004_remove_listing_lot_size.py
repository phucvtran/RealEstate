# Generated by Django 3.1.5 on 2021-02-19 00:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_auto_20210218_1619'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='lot_size',
        ),
    ]