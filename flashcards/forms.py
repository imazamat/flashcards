from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from .models import Collection, FlashCard
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CollectionForm(ModelForm):
    class Meta:
        model = Collection
        fields = ["name"]


class FlashCardForm(ModelForm):
    class Meta:
        model = FlashCard
        fields = [
            "word",
            "definition",
            "difficulty",
        ]

    def clean(self):
        super(FlashCardForm, self).clean()
        word = self.cleaned_data.get("word")
        definition = self.cleaned_data.get("definition")
        if word.strip():
            self._errors["word"] = self.error_class(["some error"])
        if definition.strip():
            self._errors["definition"] = self.error_class(["some def error"])

        return self.cleaned_data


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'username', 'email', 'password1', 'password2']
        labels = {
            'first_name': "Name",
            'username': "Username",
            'email': "Email",
        }

    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)

        for key, field in self.fields.items():
            field.widget.attrs.update({"class": 'form-control'})