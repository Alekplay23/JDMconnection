# Generated by Django 4.2.7 on 2023-11-21 02:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0006_sale_salesdetail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cars',
            old_name='quantity',
            new_name='stock',
        ),
    ]
