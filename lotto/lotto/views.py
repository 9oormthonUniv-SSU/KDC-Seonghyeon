from django.shortcuts import render
from django.http import HttpResponse
from .models import GuessNumbers
from .forms import PostForm

def index(request):
  lottos = GuessNumbers.objects.all() 
  return render(request, 'lotto/default.html', {'lottos':lottos})

def hello(request):
  return HttpResponse("<h1 style='color:red;'>Hello, Django!</h1>")


def post(request):
  form = PostForm() # 상단 from .forms import PostForm 추가
  return render(request, "lotto/form.html", {"form": form})