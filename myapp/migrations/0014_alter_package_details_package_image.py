# Generated by Django 4.1.6 on 2023-06-09 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_package_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package_details',
            name='package_image',
            field=models.ImageField(default='', upload_to='pics'),
        ),
    ]
