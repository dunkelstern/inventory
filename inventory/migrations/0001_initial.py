# Generated by Django 3.0.4 on 2020-08-03 21:20

import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Container',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Distributor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.CharField(max_length=4096)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('changed_at', models.DateTimeField(auto_now=True)),
                ('web_link', models.URLField(blank=True, null=True)),
                ('search_link', models.URLField(blank=True, null=True, verbose_name='Use {} for search placeholder')),
                ('phone', models.CharField(blank=True, max_length=128, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Layout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.CharField(max_length=4096)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('changed_at', models.DateTimeField(auto_now=True)),
                ('data', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.CharField(max_length=4096)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('changed_at', models.DateTimeField(auto_now=True)),
                ('web_link', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Workshop',
            fields=[
                ('container_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='inventory.Container')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.CharField(max_length=4096)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('changed_at', models.DateTimeField(auto_now=True)),
            ],
            bases=('inventory.container',),
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.PositiveIntegerField(verbose_name='Index of compartment in layout')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.CharField(max_length=4096)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('changed_at', models.DateTimeField(auto_now=True)),
                ('metadata', django.contrib.postgres.fields.jsonb.JSONField(verbose_name='Custom metadata, used by templates')),
                ('distributor_item_no', models.CharField(blank=True, max_length=255, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=3, max_digits=7, null=True)),
                ('last_ordered_on', models.DateField(blank=True, null=True)),
                ('documentation', django.contrib.postgres.fields.ArrayField(base_field=models.FileField(upload_to=''), size=None)),
                ('container', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_related', to='inventory.Container')),
                ('distributor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='inventory.Distributor')),
                ('manufacturer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='inventory.Manufacturer')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='container',
            name='layout',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='inventory.Layout'),
        ),
        migrations.CreateModel(
            name='Box',
            fields=[
                ('container_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='inventory.Container')),
                ('index', models.PositiveIntegerField(verbose_name='Index of compartment in layout')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.CharField(max_length=4096)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('changed_at', models.DateTimeField(auto_now=True)),
                ('container', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='box_related', to='inventory.Container')),
            ],
            options={
                'abstract': False,
            },
            bases=('inventory.container', models.Model),
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('container_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='inventory.Container')),
                ('index', models.PositiveIntegerField(verbose_name='Index of compartment in layout')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.CharField(max_length=4096)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('changed_at', models.DateTimeField(auto_now=True)),
                ('container', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='area_related', to='inventory.Container')),
            ],
            options={
                'abstract': False,
            },
            bases=('inventory.container', models.Model),
        ),
    ]
