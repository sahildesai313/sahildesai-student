# Generated by Django 4.2.1 on 2023-06-07 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_remove_package_details_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='package_details',
            name='image_identifier',
            field=models.IntegerField(default=2, unique=True),
            preserve_default=False,
        ),
    ]