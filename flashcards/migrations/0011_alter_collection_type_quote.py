# Generated by Django 4.1.7 on 2023-04-15 15:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("flashcards", "0010_delete_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="collection",
            name="type",
            field=models.CharField(
                choices=[("public", "Public"), ("private", "Private")],
                default="private",
                max_length=7,
            ),
        ),
        migrations.CreateModel(
            name="Quote",
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
                ("text", models.TextField()),
                ("author", models.CharField(max_length=255)),
                (
                    "created_by",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "likes",
                    models.ManyToManyField(
                        related_name="quote_like", to=settings.AUTH_USER_MODEL
                    ),
                ),
            ],
        ),
    ]