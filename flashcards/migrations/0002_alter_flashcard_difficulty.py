# Generated by Django 4.1.7 on 2023-03-31 05:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("flashcards", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="flashcard",
            name="difficulty",
            field=models.CharField(
                choices=[("Easy", "Easy"), ("Good", "Good"), ("Hard", "Hard")],
                default="Hard",
                max_length=4,
            ),
        ),
    ]
