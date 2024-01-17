from django.http import JsonResponse
from django.shortcuts import render


def home(request):
    data = {'message': 'Hello from the home page!'}
    return JsonResponse(data)


def scorecard(request):
    data = {'message': 'Hello from the scorecard page!'}
    return JsonResponse(data)


def my_page(request):
    return render(request, 'my_page.html')
