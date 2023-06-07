# Generated by Django 4.1.6 on 2023-06-06 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_change_user_model_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='package_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package_name', models.CharField(max_length=20)),
                ('no_of_day', models.IntegerField()),
                ('package_description', models.TextField()),
                ('package_price', models.IntegerField()),
            ],
        ),
    ]