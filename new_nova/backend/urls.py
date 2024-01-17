from django.urls import path
from .views import home, scorecard, my_page, players

urlpatterns = [
    path('', home, name='home'),
    path('scorecard/', scorecard, name='scorecard'),
    path('my-page/', my_page, name='my-page'),
    path('players/', players, name='players')
]
