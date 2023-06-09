# Generated by Django 4.1.7 on 2023-04-06 10:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("flashcards", "0005_alter_collection_created_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="flashcard",
            name="difficulty",
            field=models.CharField(
                choices=[("1", "Easy"), ("2", "Good"), ("3", "Hard")],
                default="3",
                max_length=1,
            ),
        ),
    ]
