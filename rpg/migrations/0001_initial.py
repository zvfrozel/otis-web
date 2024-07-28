# Generated by Django 4.0.8 on 2022-11-15 12:37

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import dashboard.models
import rpg.models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("roster", "0001_squashed_0102_alter_studentregistration_agreement_form"),
        ("core", "0001_squashed_0054_userprofile_use_twemoji"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Achievement",
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
                (
                    "code",
                    models.CharField(
                        max_length=96,
                        null=True,
                        unique=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="24-26 char hex string",
                                regex="^[a-f0-9]{24,26}$",
                            )
                        ],
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Name of the achievement", max_length=128
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        help_text="Image for the obtained achievement, at most 1MB.",
                        null=True,
                        upload_to=rpg.models.achievement_image_file_name,
                        validators=[dashboard.models.validate_at_most_1mb],
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        help_text="Text shown beneath this achievement for students who obtain it.",
                    ),
                ),
                (
                    "solution",
                    models.TextField(
                        blank=True,
                        help_text="Description of where the diamond is hidden",
                    ),
                ),
                (
                    "active",
                    models.BooleanField(
                        default=True,
                        help_text="Whether the code is active right now",
                    ),
                ),
                (
                    "diamonds",
                    models.SmallIntegerField(
                        default=0,
                        help_text="Number of diamonds for this achievement",
                    ),
                ),
                (
                    "always_show_image",
                    models.BooleanField(
                        default=False,
                        help_text="If enabled, always show the achievement image, even if no one earned the diamond yet.",
                        verbose_name="Reveal",
                    ),
                ),
                (
                    "creator",
                    models.ForeignKey(
                        blank=True,
                        help_text="User who owns this achievement",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "dashboard_achievement",
            },
        ),
        migrations.CreateModel(
            name="BonusLevel",
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
                (
                    "level",
                    models.PositiveSmallIntegerField(help_text="Level to spawn at"),
                ),
                ("active", models.BooleanField(default=True)),
                (
                    "group",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.unitgroup",
                    ),
                ),
            ],
            options={
                "db_table": "dashboard_bonuslevel",
            },
        ),
        migrations.CreateModel(
            name="Level",
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
                (
                    "threshold",
                    models.IntegerField(
                        help_text="The number of the level", unique=True
                    ),
                ),
                (
                    "name",
                    models.CharField(help_text="The name of the level", max_length=128),
                ),
            ],
            options={
                "db_table": "dashboard_level",
            },
        ),
        migrations.CreateModel(
            name="QuestComplete",
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
                (
                    "title",
                    models.CharField(help_text="A summary", max_length=160),
                ),
                (
                    "spades",
                    models.PositiveSmallIntegerField(
                        help_text="The number of spades granted"
                    ),
                ),
                (
                    "timestamp",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="The time the achievement was granted",
                    ),
                ),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("PR", "Pull request"),
                            ("BR", "Bug report"),
                            ("WK", "Wiki bonus"),
                            ("US", "USEMO Score"),
                            ("UG", "USEMO Grading"),
                            ("MS", "Miscellaneous"),
                        ],
                        default="MS",
                        max_length=4,
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        help_text="Student obtaining this reward",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="roster.student",
                    ),
                ),
            ],
            options={
                "db_table": "dashboard_questcomplete",
            },
        ),
        migrations.CreateModel(
            name="PalaceCarving",
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
                (
                    "display_name",
                    models.CharField(
                        help_text="How you would like your name to be displayed in the Ruby Palace.",
                        max_length=128,
                    ),
                ),
                (
                    "message",
                    models.TextField(
                        blank=True,
                        help_text="You can write a message here",
                        max_length=1024,
                    ),
                ),
                (
                    "hyperlink",
                    models.URLField(
                        blank=True, help_text="An external link of your choice"
                    ),
                ),
                (
                    "visible",
                    models.BooleanField(
                        default=True,
                        help_text="Uncheck to hide your carving altogether (can change your mind later)",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        help_text="Optional small photo that will appear next to your carving, no more than 1 megabyte",
                        null=True,
                        upload_to=rpg.models.palace_image_file_name,
                        validators=[dashboard.models.validate_at_most_1mb],
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "dashboard_palacecarving",
            },
        ),
        migrations.CreateModel(
            name="BonusLevelUnlock",
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
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                (
                    "bonus",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="rpg.bonuslevel",
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="roster.student",
                    ),
                ),
            ],
            options={
                "db_table": "dashboard_bonuslevelunlock",
            },
        ),
        migrations.CreateModel(
            name="AchievementUnlock",
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
                (
                    "timestamp",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="The time the achievement was granted",
                    ),
                ),
                (
                    "achievement",
                    models.ForeignKey(
                        help_text="The achievement that was obtained",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="rpg.achievement",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        help_text="The user who unlocked the achievement",
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "dashboard_achievementunlock",
                "unique_together": {("user", "achievement")},
            },
        ),
    ]
