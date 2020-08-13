# Generated by Django 3.0.5 on 2020-07-09 21:55

from django.db import migrations


def load_location(apps, schema_editor):
    Location_legacy = apps.get_model("hueb_legacy_latein", "LocationNew")
    Country = apps.get_model("hueb20", "Country")
    Location = apps.get_model("hueb20", "Location")
    Source = apps.get_model("hueb20", "SourceReference")

    for legacy_location in Location_legacy.objects.all():
        source = Source()
        source.app = "hueb_legacy_latein"
        source.location_ref = legacy_location
        source.save()

        new_location = Location()
        new_location.source = source

        new_location.name = legacy_location.name
        new_location.adress = legacy_location.adress
        new_location.hostname = legacy_location.hostname
        new_location.ip = legacy_location.ip
        new_location.z3950_gateway = legacy_location.z3950_gateway

        if legacy_location.country is not None:
            new_country_source_id = (
                Source.objects.filter(app="hueb_legacy_latein")
                .get(country_ref=legacy_location.country)
                .id
            )

            new_location.country = Country.objects.get(source=new_country_source_id)

        else:
            new_location.country = None

        new_location.save()


def unload_location(apps, schema_editor):
    Source = apps.get_model("hueb20", "SourceReference")
    Source.objects.filter(app="hueb_legacy_latein").filter(
        location_ref__isnull=False
    ).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("hueb20", "0008_load_ddc"),
        ("hueb_legacy_latein", "0005_auto_20200709_2025"),
    ]

    operations = [migrations.RunPython(load_location, unload_location)]