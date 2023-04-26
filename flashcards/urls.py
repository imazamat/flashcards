from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("edit/<int:id>/", edit_collection, name="edit-collection"),
    path("delete/<int:id>/", delete_collection, name="delete-collection"),
    path("<int:id>/", detail_flashcard, name="detail-flashcard"),
    path(
        "<int:id>/edit-flashcard/<int:flashcard_id>/",
        edit_flashcard,
        name="edit-flashcard",
    ),
    path(
        "delete-flashcard/<int:flashcard_id>/",
        delete_flashcard,
        name="delete-flashcard",
    ),
    path("<int:id>/test/", test, name="test"),
    path('login/', login_, name='login'),
    path('logout/', logout_, name='logout'),
    path('register/', register_, name='register'),
    path('get-quote/', get_quote, name='get-quote'),
    path('quote-like/', quote_like, name='quote-like'),
]
