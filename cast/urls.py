from django.urls import path

from . import views

app_name = 'cast'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:movie_id>/', views.detail, name='detail'),
]