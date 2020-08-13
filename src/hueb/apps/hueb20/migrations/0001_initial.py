# Generated by Django 3.0.5 on 2020-07-16 22:42

import django.contrib.postgres.fields.ranges
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("hueb_legacy_latein", "0005_auto_20200709_2025"),
    ]

    operations = [
        migrations.CreateModel(
            name="Archive",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("signatur", models.CharField(max_length=255)),
                ("link", models.CharField(blank=True, max_length=255, null=True)),
                ("app", models.CharField(max_length=255)),
                (
                    "locAssign_ref",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="hueb_legacy_latein.LocAssign",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Country",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("country", models.CharField(max_length=255)),
                ("app", models.CharField(max_length=255)),
                (
                    "country_ref",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="country_ref",
                        to="hueb_legacy_latein.Country",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="DdcGerman",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("ddc_number", models.CharField(max_length=3)),
                ("ddc_name", models.CharField(max_length=255)),
                ("app", models.CharField(max_length=255)),
                (
                    "ddc_ref",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="hueb_legacy_latein.DdcGerman",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Person",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(blank=True, max_length=255, null=True)),
                ("comment", models.TextField(blank=True, null=True)),
                ("is_alias", models.BooleanField(blank=True, null=True)),
                ("app", models.CharField(max_length=255)),
                (
                    "alias",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="hueb20.Person",
                    ),
                ),
                (
                    "author_ref",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="hueb_legacy_latein.AuthorNew",
                    ),
                ),
                (
                    "publisherOriginal_ref",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="hueb_legacy_latein.OriginalNew",
                    ),
                ),
                (
                    "publisherTranslation_ref",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="hueb_legacy_latein.TranslationNew",
                    ),
                ),
                (
                    "translator_ref",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="hueb_legacy_latein.TranslatorNew",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="YearRange",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                (
                    "timerange",
                    django.contrib.postgres.fields.ranges.IntegerRangeField(
                        blank=True, null=True
                    ),
                ),
                ("start_uncertainty", models.IntegerField(blank=True, null=True)),
                ("end_uncertainty", models.IntegerField(blank=True, null=True)),
                ("parsed_string", models.TextField(blank=True, null=True)),
                ("app", models.CharField(max_length=255)),
                (
                    "author_ref",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="hueb_legacy_latein.AuthorNew",
                    ),
                ),
                (
                    "person_lifetime",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="lifetime",
                        to="hueb20.Person",
                    ),
                ),
                (
                    "translator_ref",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="hueb_legacy_latein.TranslatorNew",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Location",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=255, null=True)),
                ("adress", models.TextField(blank=True, null=True)),
                ("hostname", models.CharField(blank=True, max_length=255, null=True)),
                ("ip", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "z3950_gateway",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("app", models.CharField(max_length=255)),
                (
                    "country",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="hueb20.Country",
                    ),
                ),
                (
                    "location_ref",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="hueb_legacy_latein.LocationNew",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Language",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("language", models.CharField(max_length=255)),
                ("app", models.CharField(max_length=255)),
                (
                    "language_ref",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="language_ref",
                        to="hueb_legacy_latein.Language",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Document",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("title", models.TextField(blank=True, null=True)),
                ("subtitle", models.TextField(blank=True, null=True)),
                ("year", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "published_location",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("edition", models.TextField(blank=True, null=True)),
                ("real_year", models.IntegerField(blank=True, null=True)),
                ("app", models.CharField(blank=True, max_length=255, null=True)),
                ("archive", models.ManyToManyField(to="hueb20.Archive")),
                (
                    "authors",
                    models.ManyToManyField(
                        related_name="DocumentAuthor", to="hueb20.Person"
                    ),
                ),
                (
                    "country",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="hueb20.Country",
                    ),
                ),
                (
                    "ddc",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="hueb20.DdcGerman",
                    ),
                ),
                (
                    "language",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="hueb20.Language",
                    ),
                ),
                (
                    "origAssign_ref",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="hueb_legacy_latein.OrigAssign",
                    ),
                ),
                (
                    "originalAuthor_ref",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="hueb_legacy_latein.OriginalNewAuthorNew",
                    ),
                ),
                (
                    "original_ref",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="hueb_legacy_latein.OriginalNew",
                    ),
                ),
                (
                    "publishers",
                    models.ManyToManyField(
                        related_name="DocumentPublishers", to="hueb20.Person"
                    ),
                ),
                (
                    "translated_from",
                    models.ManyToManyField(
                        related_name="_document_translated_from_+", to="hueb20.Document"
                    ),
                ),
                (
                    "translated_to",
                    models.ManyToManyField(
                        related_name="_document_translated_to_+", to="hueb20.Document"
                    ),
                ),
                (
                    "translationTranslator_ref",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="hueb_legacy_latein.TranslationNewTranslatorNew",
                    ),
                ),
                (
                    "translation_ref",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="hueb_legacy_latein.TranslationNew",
                    ),
                ),
            ],
        ),
    ]