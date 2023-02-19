from django.shortcuts import get_object_or_404, render

from base.models import Movie

def index(request):
    latest_movie_list = Movie.objects.order_by('-updated_at')[:5]
    context = {
        'latest_movie_list': latest_movie_list,
    }
    return render(request, 'movies/index.html', context)

def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'movies/detail.html', {'movie': movie})
