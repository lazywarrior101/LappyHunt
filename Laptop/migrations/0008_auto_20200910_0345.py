# Generated by Django 3.0.9 on 2020-09-09 22:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Laptop', '0007_auto_20200910_0240'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='item',
            new_name='laptop',
        ),
    ]
