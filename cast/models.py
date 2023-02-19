import datetime

from django.db import models
from django.utils import timezone


class Person(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    created_at = models.DateTimeField('date create')
    updated_at = models.DateTimeField('date update')

    def __str__(self):
        return self.surname + " " + self.name


class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField('date create')
    updated_at = models.DateTimeField('date update')
    
    def __str__(self):
        return self.title


class Character(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    role = models.CharField(max_length=200)
    created_at = models.DateTimeField('date create')
    updated_at = models.DateTimeField('date update')

    def __str__(self):
        return self.role + " : " + self.person.surname
