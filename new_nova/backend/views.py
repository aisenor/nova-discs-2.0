from django.core.mail.backends import console
from django.http import JsonResponse
from django.shortcuts import render
from django.core.serializers import serialize

from .models.players import Players


def home(request):
    data = {'message': 'Hello from the home page!'}
    return JsonResponse(data)


def scorecard(request):
    data = {'message': 'Hello from the scorecard page!'}
    return JsonResponse(data)


def my_page(request):
    return render(request, 'my_page.html')


def players(request):
    players_data = serialize('json', Players.objects.all())
    data = {'players': players_data}
    return JsonResponse(data, safe=False)
