# Generated by Django 4.2.7 on 2023-11-19 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_remove_cars_image_url_cars_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cars',
            old_name='count',
            new_name='quantity',
        ),
    ]
