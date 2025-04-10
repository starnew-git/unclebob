from django.contrib import admin
from .models import Version, Testament, Book, Verse

admin.site.register(Version)
admin.site.register(Testament)
admin.site.register(Book)
admin.site.register(Verse)