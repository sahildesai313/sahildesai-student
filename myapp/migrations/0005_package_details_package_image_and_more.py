# Generated by Django 4.1.6 on 2023-06-07 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_package_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='package_details',
            name='package_image',
            field=models.ImageField(default='', upload_to='photos'),
        ),
        migrations.AlterField(
            model_name='package_details',
            name='no_of_day',
            field=models.IntegerField(default=''),
        ),
        migrations.AlterField(
            model_name='package_details',
            name='package_description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='package_details',
            name='package_price',
            field=models.IntegerField(default=''),
        ),
    ]