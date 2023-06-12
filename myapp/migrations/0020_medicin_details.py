# Generated by Django 4.2.1 on 2023-06-12 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0019_alter_package_details_package_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medicin_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Medicin_name', models.CharField(max_length=100)),
                ('Medicin_image', models.ImageField(upload_to='images')),
                ('Do_description', models.TextField(default='')),
                ('Medicin_price', models.IntegerField(default='')),
            ],
        ),
    ]