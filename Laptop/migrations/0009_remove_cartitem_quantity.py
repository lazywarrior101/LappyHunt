# Generated by Django 3.0.9 on 2020-09-09 22:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Laptop', '0008_auto_20200910_0345'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='quantity',
        ),
    ]
