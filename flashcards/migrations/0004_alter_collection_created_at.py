# Generated by Django 4.1.7 on 2023-04-06 07:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("flashcards", "0003_alter_flashcard_difficulty"),
    ]

    operations = [
        migrations.AlterField(
            model_name="collection",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
