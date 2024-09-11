from django.urls import path
from . import views

urlpatterns = [
  # localhost:8000/polls 이후의 URL은 여기서 핸들링
  path('', views.indx, name='index'), 
]