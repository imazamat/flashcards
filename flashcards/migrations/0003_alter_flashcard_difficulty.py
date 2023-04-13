# Generated by Django 4.1.7 on 2023-03-31 11:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("flashcards", "0002_alter_flashcard_difficulty"),
    ]

    operations = [
        migrations.AlterField(
            model_name="flashcard",
            name="difficulty",
            field=models.CharField(
                choices=[("E", "Easy"), ("G", "Good"), ("H", "Hard")],
                default="H",
                max_length=1,
            ),
        ),
    ]