# Generated by Django 3.0.5 on 2020-08-11 20:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("hueb20", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="document", name="origAssign_ref",),
    ]