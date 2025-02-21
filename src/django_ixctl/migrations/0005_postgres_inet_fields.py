# Generated by Django 3.2.4 on 2021-06-28 12:25

import netfields.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("django_ixctl", "0004_alter_internetexchange_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="internetexchangemember",
            name="ipaddr4",
            field=netfields.fields.InetAddressField(
                blank=True, max_length=39, null=True
            ),
        ),
        migrations.AlterField(
            model_name="internetexchangemember",
            name="ipaddr6",
            field=netfields.fields.InetAddressField(
                blank=True, max_length=39, null=True
            ),
        ),
        migrations.AlterField(
            model_name="internetexchangemember",
            name="macaddr",
            field=netfields.fields.MACAddressField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="routeserver",
            name="router_id",
            field=netfields.fields.InetAddressField(
                help_text="Router Id", max_length=39
            ),
        ),
    ]
