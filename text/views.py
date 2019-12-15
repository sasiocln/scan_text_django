from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
from .models import Photo
import pytesseract
from PIL import Image


# Create your views here.
def image_view(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('text')
    else:
        form = ImageForm()
    return render(request, 'upload.html', {'form': form})


def success(request):
    return HttpResponse('successfully uploaded')


def show_extract_text(request):
    photo = Photo.objects.last()
    if photo.language == True:
        photo.text_of_image = get_text_rus(photo.photo.path)
    else:
        photo.text_of_image = get_text(photo.photo.path)
    photo.save()
    return render(request, 'image_text.html', {'photo': photo})


def get_text(file):
    text = pytesseract.image_to_string(Image.open(file))
    return text


def get_text_rus(file):
    text = pytesseract.image_to_string(Image.open(file), lang="rus")
    return text