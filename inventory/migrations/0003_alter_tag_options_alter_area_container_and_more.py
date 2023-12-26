# Generated by Django 5.0 on 2023-12-26 00:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("inventory", "0002_base_data"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="tag",
            options={"ordering": ["name", "pk"]},
        ),
        migrations.AlterField(
            model_name="area",
            name="container",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="%(class)s_related",
                to="inventory.container",
            ),
        ),
        migrations.AlterField(
            model_name="box",
            name="container",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="%(class)s_related",
                to="inventory.container",
            ),
        ),
        migrations.AlterField(
            model_name="item",
            name="container",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="%(class)s_related",
                to="inventory.container",
            ),
        ),
    ]