# Generated by Django 4.1.6 on 2023-06-09 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_grocery_details_delete_package_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='Package_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package_name', models.CharField(max_length=20)),
                ('package_image', models.ImageField(default='', upload_to='photos')),
                ('no_of_day', models.IntegerField(default='')),
                ('package_description', models.TextField(default='')),
                ('package_price', models.IntegerField(default='')),
            ],
        ),
    ]