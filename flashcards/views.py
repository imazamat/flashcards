import json
from django.core import serializers
from pyexpat.errors import messages
from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Collection, FlashCard
from .forms import *


# Create your views here.

def index(request):
    ctx = {}

    if request.method == "GET":
        if request.user.is_authenticated:
            collections = Collection.objects.filter(owner_id=request.user.id).order_by('-created_at')
        else:
            collections = Collection.objects.filter(type='0').order_by('-created_at')

        qs_json = json.dumps(list(collections.values('id', 'name')), cls=DjangoJSONEncoder)

        ctx['collections'] = collections
        ctx['qs_json'] = qs_json

        return render(
            request,
            "flashcards/index.html",
            ctx,
        )
    if request.method == "POST":
        form = CollectionForm(request.POST)
        if form.is_valid():
            obj = Collection()
            obj.name = request.POST['name']
            obj.type = request.POST['type']
            obj.owner_id = request.POST['owner_id']
            obj.save()
            return redirect("/")
        else:
            collections = Collection.objects.all().order_by('-created_at')
            print("rendered")
            return render(
                request, "flashcards/index.html", {"collections": collections}
            )


@login_required(login_url='login')
def edit_collection(request, id):
    if request.method == "GET":
        collection = Collection.objects.get(id=id)
        return render(request, "flashcards/edit.html", {"collection": collection})
    if request.method == "POST":
        collection = Collection.objects.get(id=id)
        form = CollectionForm(request.POST, instance=collection)
        if form.is_valid():
            collection = Collection.objects.get(id=id)
            collection.name = request.POST['name']
            collection.type = request.POST['type']
            collection.owner_id = request.POST['owner_id']
            collection.save()
            return redirect("/")
        else:
            form = CollectionForm()
            return render(request, "flashcards/edit.html", {"form": form})


@login_required(login_url='login')
def delete_collection(request, id):
    collection = Collection.objects.get(id=id)
    collection.delete()
    return redirect("/")


def detail_flashcard(request, id):
    if request.method == "GET":
        flashcards = FlashCard.objects.filter(collection_id=id).order_by("-created_at")
        collection_owner_id = Collection.objects.get(id=id).owner_id

        return render(
            request,
            "flashcards/detail-flashcard.html",
            {"flashcards": flashcards, "collection_id": id, "collection_owner_id": collection_owner_id},
        )
    if request.method == "POST":
        flashcard = FlashCard()
        flashcard.word = request.POST["word"]
        flashcard.definition = request.POST["definition"]
        flashcard.difficulty = request.POST["difficulty"]
        flashcard.collection_id = id
        flashcard.save()
        return redirect(f"/{id}/")
    else:
        return render(request, "flashcards/detail-flashcard.html")


@login_required(login_url='login')
def edit_flashcard(request, id, flashcard_id):
    if request.method == "GET":
        flashcard = FlashCard.objects.get(id=flashcard_id)
        return render(
            request,
            "flashcards/edit-flashcard.html",
            {"flashcard": flashcard, "collection_id": id},
        )

    if request.method == "POST":
        try:
            flashcard = FlashCard.objects.get(id=flashcard_id)
            flashcard.word = request.POST["word"]
            flashcard.definition = request.POST["definition"]
            flashcard.difficulty = request.POST["difficulty"]
            flashcard.collection_id = id
            flashcard.save()
            return redirect(f"/{flashcard.collection_id}/")
        except:
            raise Exception("Invalid form")


@login_required(login_url='login')
def delete_flashcard(request, flashcard_id):
    flashcard = FlashCard.objects.get(id=flashcard_id)
    flashcard.delete()
    return redirect(f"/{flashcard.collection_id}/")


def test(request, id):
    collection_name = Collection.objects.get(id=id).name
    if request.method == "GET":
        return render(
            request,
            "flashcards/test.html",
            {"collection_id": id, "collection_name": collection_name},
        )


def login_(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/')
        else:
            form = CustomUserCreationForm()
            return render(request, 'flashcards/login.html', {'form': form})

    if request.method == 'POST':
        username = request.POST.get('username', False)
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.warning(request, 'Invalid username or password')
            form = CustomUserCreationForm()
            return render(request, 'flashcards/login.html', {'form': form})


def logout_(request):
    logout(request)
    return redirect('/')


def register_(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.first_name = user.first_name.capitalize()
            user.username = user.username.lower()
            user.email = user.email.lower()
            user.save()

            login(request, user)

            messages.success(request, "User succesfully created")
            return redirect('/')
        else:
            messages.warning(request, 'Invalid credentials')
            form = CustomUserCreationForm(request.POST)
            return render(request, 'flashcards/login.html', {'form': form})
