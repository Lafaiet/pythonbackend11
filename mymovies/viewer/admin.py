from django.contrib import admin
from viewer.models import Movie, Director, Actor, Profile


admin.site.register(Movie)
admin.site.register(Director)
admin.site.register(Actor)
admin.site.register(Profile)