from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')

def counter(request):
    text = request.POST['text']
    length = len(text.strip())
    words_count = len(text.split())
    context = {"length": length, 'words_count' : words_count}
    return render(request, "counter.html", context)
