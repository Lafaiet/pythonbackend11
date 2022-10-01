from django.contrib import admin
from viewer.models import Movie, Director, Actor


admin.site.register(Movie)
admin.site.register(Director)
admin.site.register(Actor)