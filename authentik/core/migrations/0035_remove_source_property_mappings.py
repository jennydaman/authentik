# Generated by Django 5.0.2 on 2024-02-29 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("authentik_sources_ldap", "0004_remove_ldappropertymapping_object_field_and_more"),
        ("authentik_core", "0034_source_group_property_mappings_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="source",
            name="property_mappings",
        ),
    ]
