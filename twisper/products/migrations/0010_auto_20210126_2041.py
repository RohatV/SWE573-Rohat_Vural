# Generated by Django 3.1.4 on 2021-01-26 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20210126_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweets',
            name='date',
            field=models.CharField(max_length=12),
        ),
    ]
