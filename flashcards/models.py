from django.db import models
from django.contrib.auth.models import User


class Collection(models.Model):
    COLLECTION_TYPE_PUBLIC = '0'
    COLLECTION_TYPE_PRIVATE = '1'
    COLLECTION_TYPE_CHOICES = (
        (COLLECTION_TYPE_PUBLIC, 'Public'),
        (COLLECTION_TYPE_PRIVATE, 'Private'),
    )
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=7, choices=COLLECTION_TYPE_CHOICES, default=COLLECTION_TYPE_PRIVATE)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        return super(Collection, self).save(*args, **kwargs)


class FlashCard(models.Model):
    FLASHCARD_DIFFICULTY_EASY = "1"
    FLASHCARD_DIFFICULTY_GOOD = "2"
    FLASHCARD_DIFFICULTY_HARD = "3"
    FLASHCARD_DIFFICULTY_CHOICES = (
        (FLASHCARD_DIFFICULTY_EASY, "Easy"),
        (FLASHCARD_DIFFICULTY_GOOD, "Good"),
        (FLASHCARD_DIFFICULTY_HARD, "Hard"),
    )
    word = models.CharField(max_length=255, blank=False)
    definition = models.TextField(blank=False)
    difficulty = models.CharField(
        max_length=1,
        choices=FLASHCARD_DIFFICULTY_CHOICES,
        default=FLASHCARD_DIFFICULTY_HARD,
    )
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)

    def __str__(self):
        return self.word

    def save(self, *args, **kwargs):
        self.word = self.word.strip().lower()
        self.definition = self.definition.strip().lower()
        return super(FlashCard, self).save(*args, **kwargs)
