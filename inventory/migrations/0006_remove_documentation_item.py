# Generated by Django 3.0.4 on 2020-08-07 23:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_auto_20200808_0135'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='documentation',
            name='item',
        ),
    ]
