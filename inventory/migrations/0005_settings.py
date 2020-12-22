# Generated by Django 3.1.4 on 2020-12-22 19:29

from django.db import migrations, models
import django.db.models.deletion


def create_settings(apps, schema_editor):
    Settings = apps.get_model('inventory', 'Settings')
    Settings.objects.create(default_container=None)


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_auto_20201222_1858'),
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('default_container', models.ForeignKey(blank=True, default=None, help_text='Default container to display when calling the index page', null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.container')),
            ],
        ),
        migrations.RunPython(create_settings)
    ]
