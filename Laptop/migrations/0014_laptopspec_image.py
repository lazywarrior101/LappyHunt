# Generated by Django 3.0.9 on 2020-08-30 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Laptop', '0013_remove_laptopspec_harddrive'),
    ]

    operations = [
        migrations.AddField(
            model_name='laptopspec',
            name='Image',
            field=models.ImageField(blank=True, upload_to='LapImages/'),
        ),
    ]