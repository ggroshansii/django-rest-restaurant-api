# Generated by Django 3.2.8 on 2021-10-12 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='price',
            field=models.IntegerField(),
        ),
    ]
