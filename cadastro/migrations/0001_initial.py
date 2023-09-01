# Generated by Django 4.2.4 on 2023-08-31 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Stand",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("localizacao", models.CharField(max_length=100)),
                ("valor", models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name="Reserva",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("CNPJ", models.CharField(max_length=15)),
                ("nome_empresa", models.CharField(max_length=100)),
                ("categoria_empresa", models.CharField(max_length=100)),
                ("quitado", models.BooleanField()),
                (
                    "stand",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="cadastro.stand"
                    ),
                ),
            ],
        ),
    ]
