from django.http import JsonResponse


def home(request):
    data = {'message': 'Welcome to the NEW Nova Discs site!'}
    return JsonResponse(data)
