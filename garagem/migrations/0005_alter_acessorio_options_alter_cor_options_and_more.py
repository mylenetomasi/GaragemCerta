# Generated by Django 4.2.1 on 2023-05-15 01:28

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("garagem", "0004_veiculo"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="acessorio",
            options={"verbose_name": "Acessório"},
        ),
        migrations.AlterModelOptions(
            name="cor",
            options={"verbose_name_plural": "Cores"},
        ),
        migrations.AlterModelOptions(
            name="veiculo",
            options={"verbose_name": "Veículo"},
        ),
    ]
