from django.db import models
from django.contrib.auth.models import User

# Music
# User review ?
# User ?


class Director(models.Model):

    name = models.CharField(max_length=50)
    date_birth = models.DateField()
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Actor(models.Model):

    name = models.CharField(max_length=50)
    date_birth = models.DateField()
    bio = models.TextField(null=True, blank=True)
    place_birth = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class Movie(models.Model):

    title = models.CharField(max_length=100)
    release_year = models.PositiveIntegerField()
    duration = models.DurationField()
    genre = models.CharField(max_length=30)
    description = models.TextField(null=True, blank=True)
    rating = models.FloatField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now=True, null=True, blank=True)
    director = models.ForeignKey(Director, on_delete=models.DO_NOTHING, null=True, blank=True)
    actors = models.ManyToManyField(Actor, blank=True)
    # cover = models.ImageField(null=True, blank=True, upload_to='images/')

    def __str__(self):
        return self.title


class Profile(models.Model):

    intro = models.TextField(null=True, blank=True)
    watch_list = models.ManyToManyField(Movie)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    def __str__(self):
        return self.user.username


