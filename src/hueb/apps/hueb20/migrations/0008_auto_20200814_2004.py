# Generated by Django 3.0.5 on 2020-08-14 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hueb20", "0007_auto_20200814_1704"),
    ]

    operations = [
        migrations.AlterField(
            model_name="archive",
            name="app",
            field=models.CharField(
                choices=[
                    ("LATEIN", "HÜB Latein Datensatz"),
                    ("LIDOS ", "HÜB Lidos Datensatz"),
                    ("LEGACY", "HÜB Basis Datensatz"),
                    ("HUEB20", "HÜB 2020 Datensatz"),
                ],
                default="HUEB20",
                max_length=6,
            ),
        ),
        migrations.AlterField(
            model_name="country",
            name="app",
            field=models.CharField(
                choices=[
                    ("LATEIN", "HÜB Latein Datensatz"),
                    ("LIDOS ", "HÜB Lidos Datensatz"),
                    ("LEGACY", "HÜB Basis Datensatz"),
                    ("HUEB20", "HÜB 2020 Datensatz"),
                ],
                default="HUEB20",
                max_length=6,
            ),
        ),
        migrations.AlterField(
            model_name="country",
            name="country",
            field=models.CharField(help_text="Name of the country", max_length=255),
        ),
        migrations.AlterField(
            model_name="ddcgerman",
            name="app",
            field=models.CharField(
                choices=[
                    ("LATEIN", "HÜB Latein Datensatz"),
                    ("LIDOS ", "HÜB Lidos Datensatz"),
                    ("LEGACY", "HÜB Basis Datensatz"),
                    ("HUEB20", "HÜB 2020 Datensatz"),
                ],
                default="HUEB20",
                max_length=6,
            ),
        ),
        migrations.AlterField(
            model_name="document",
            name="app",
            field=models.CharField(
                choices=[
                    ("LATEIN", "HÜB Latein Datensatz"),
                    ("LIDOS ", "HÜB Lidos Datensatz"),
                    ("LEGACY", "HÜB Basis Datensatz"),
                    ("HUEB20", "HÜB 2020 Datensatz"),
                ],
                default="HUEB20",
                max_length=6,
            ),
        ),
        migrations.AlterField(
            model_name="language",
            name="app",
            field=models.CharField(
                choices=[
                    ("LATEIN", "HÜB Latein Datensatz"),
                    ("LIDOS ", "HÜB Lidos Datensatz"),
                    ("LEGACY", "HÜB Basis Datensatz"),
                    ("HUEB20", "HÜB 2020 Datensatz"),
                ],
                default="HUEB20",
                max_length=6,
            ),
        ),
        migrations.AlterField(
            model_name="location",
            name="app",
            field=models.CharField(
                choices=[
                    ("LATEIN", "HÜB Latein Datensatz"),
                    ("LIDOS ", "HÜB Lidos Datensatz"),
                    ("LEGACY", "HÜB Basis Datensatz"),
                    ("HUEB20", "HÜB 2020 Datensatz"),
                ],
                default="HUEB20",
                max_length=6,
            ),
        ),
        migrations.AlterField(
            model_name="person",
            name="app",
            field=models.CharField(
                choices=[
                    ("LATEIN", "HÜB Latein Datensatz"),
                    ("LIDOS ", "HÜB Lidos Datensatz"),
                    ("LEGACY", "HÜB Basis Datensatz"),
                    ("HUEB20", "HÜB 2020 Datensatz"),
                ],
                default="HUEB20",
                max_length=6,
            ),
        ),
        migrations.AlterField(
            model_name="yearrange",
            name="app",
            field=models.CharField(
                choices=[
                    ("LATEIN", "HÜB Latein Datensatz"),
                    ("LIDOS ", "HÜB Lidos Datensatz"),
                    ("LEGACY", "HÜB Basis Datensatz"),
                    ("HUEB20", "HÜB 2020 Datensatz"),
                ],
                default="HUEB20",
                max_length=6,
            ),
        ),
    ]