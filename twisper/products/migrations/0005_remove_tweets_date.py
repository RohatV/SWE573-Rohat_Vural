# Generated by Django 3.1.4 on 2021-01-26 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20210125_2145'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tweets',
            name='date',
        ),
    ]
