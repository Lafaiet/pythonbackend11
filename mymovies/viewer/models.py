from django.db import models

# Movie
# Director
# Star
# Genre ?
# Music
# User review
# User


class Movie(models.Model):

    title = models.CharField(max_length=100)
    release_year = models.PositiveIntegerField()
    duration = models.DurationField()
    genre = models.CharField(max_length=30)
    description = models.TextField()

    # director ?
    # actors ?
