# backend/admin.py

from django.contrib import admin
from .models.putting_league import PuttingLeague
from .models.players import Players

admin.site.register(PuttingLeague)
admin.site.register(Players)
