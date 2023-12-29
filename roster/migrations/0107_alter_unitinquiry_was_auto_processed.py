# Generated by Django 4.2.7 on 2023-12-05 02:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("roster", "0106_auto_20231204_2144"),
    ]

    operations = [
        migrations.AlterField(
            model_name="unitinquiry",
            name="was_auto_processed",
            field=models.BooleanField(
                default=False,
                help_text="Whether the inquiry was automatically accepted or rejected by auto-criteria.",
                verbose_name="Auto",
            ),
        ),
    ]