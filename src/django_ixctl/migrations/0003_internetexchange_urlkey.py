# Generated by Django 2.2.14 on 2020-07-28 18:01

from django.db import migrations, models
import django_ixctl.models


class Migration(migrations.Migration):

    dependencies = [
        ("django_ixctl", "0002_auto_20200728_1756"),
    ]

    operations = [
        migrations.AddField(
            model_name="internetexchange",
            name="urlkey",
            field=models.CharField(
                default=django_ixctl.models.generate_secret, max_length=255, unique=True
            ),
        ),
    ]
