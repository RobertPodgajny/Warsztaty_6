from django.contrib import admin

from movies.models import Person, Movie

admin.site.register(Person)
admin.site.register(Movie)
