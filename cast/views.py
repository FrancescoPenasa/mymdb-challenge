from django.shortcuts import render

from .models import Person, Movie, Character

def index(request):
    latest_movie_list = Movie.objects.order_by('-updated_at')[:5]
    context = {
        'latest_movie_list': latest_movie_list,
    }
    return render(request, 'cast/index.html', context)
