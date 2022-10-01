from django.contrib import admin

# Register your models here.
from api.models import Anime, Rating

admin.site.register(Anime)
admin.site.register(Rating)
