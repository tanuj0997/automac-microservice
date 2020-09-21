# Generated by Django 3.1.1 on 2020-09-18 08:46

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Manufacturer",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created At"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated At"),
                ),
                (
                    "country",
                    models.IntegerField(
                        choices=[
                            (1, "United State"),
                            (91, "India"),
                            (93, "Afghanistan"),
                            (48, "Poland"),
                            (86, "China"),
                            (33, "France"),
                            (81, "Japan"),
                            (51, "Peru"),
                            (92, "Pakistan"),
                            (7, "Rasia"),
                        ],
                        default=1,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        choices=[
                            ("UNITED_STATES", "United State"),
                            ("INDIA", "India"),
                            ("AFGHANISTAN", "Afghanistan"),
                            ("POLAND", "Poland"),
                            ("CHINA", "China"),
                            ("FRANCE", "France"),
                            ("JAPAN", "Japan"),
                            ("PERU", "Peru"),
                            ("PAKISTAN", "Pakistan"),
                            ("RASIA", "Rasia"),
                        ],
                        default="UNITED_STATES",
                        max_length=52,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="CarDetail",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created At"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated At"),
                ),
                ("name", models.CharField(max_length=52, unique=True)),
                (
                    "model",
                    models.CharField(
                        choices=[
                            ("SEDAN", "SEDAN"),
                            ("MPV", "MPV"),
                            ("SUV", "SUV"),
                            ("COUPE", "COUPE"),
                            ("CROSSOVER", "CROSSOVER"),
                        ],
                        max_length=12,
                        null=True,
                    ),
                ),
                (
                    "color",
                    models.CharField(
                        choices=[
                            ("R", "Red"),
                            ("BL", "Black"),
                            ("G", "Green"),
                            ("W", "White"),
                            ("BLU", "Blue"),
                        ],
                        max_length=3,
                        null=True,
                    ),
                ),
                ("door", models.IntegerField()),
                ("owner", models.CharField(max_length=26)),
                (
                    "manufacturer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="cars",
                        to="auto_manufac.manufacturer",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
