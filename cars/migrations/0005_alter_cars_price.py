# Generated by Django 4.2.7 on 2023-11-20 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_alter_cars_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cars',
            name='price',
            field=models.FloatField(),
        ),
    ]
