from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
  # localhost:8000/polls 이후의 URL은 여기서 핸들링
  path('', views.index, name='index'),
  path('<int:question_id>/', views.detail, name='detail'),
  path('<int:question_id>/results/', views.results, name='results'),
  path('<int:question_id>/vote/', views.vote, name='vote'),
]