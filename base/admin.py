from django.contrib import admin

from .models import Person, Movie, Character, Review

admin.site.register(Person)
admin.site.register(Movie)
admin.site.register(Character)
admin.site.register(Review)