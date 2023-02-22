from django.contrib.auth.models import User, Group
from base.models import Person, Movie, Character, Review
from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view
from .serializers import UserSerializer, GroupSerializer, PersonSerializer, MovieSerializer, CharacterSerializer, ReviewSerializer
import datetime

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class PersonViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows persons to be viewed.
    """
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = [permissions.AllowAny]

class MovieViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows movie to be viewed.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [permissions.AllowAny]

class CharacterViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows character to be viewed.
    """
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    permission_classes = [permissions.AllowAny]

class ReviewViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows character to be viewed.
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.AllowAny]
