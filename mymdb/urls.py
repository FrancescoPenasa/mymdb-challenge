"""mymdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from apis import views

router = routers.DefaultRouter()
router.register(r'api/v1/users', views.UserViewSet)
router.register(r'api/v1/groups', views.GroupViewSet)
router.register(r'api/v1/persons', views.PersonViewSet)
router.register(r'api/v1/movies', views.MovieViewSet)
router.register(r'api/v1/characters', views.CharacterViewSet)
router.register(r'api/v1/reviews', views.ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('cast/', include('cast.urls')),
    path('movies/', include('movies.urls')),
    path('reviews/', include('reviews.urls')),
    path('admin/', admin.site.urls),
]
