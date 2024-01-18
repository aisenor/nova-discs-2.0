from django.urls import path
from .views import home, scorecard, my_page

from api.players.list_view import PlayersListView
from api.players.detail_view import PlayersDetailView
from api.putting_league.list_view import PuttingLeagueListView
from api.putting_league.detail_view import PuttingLeagueDetailView
from api.standings.list_view import StandingsAPIView

urlpatterns = [
    path('', home, name='home'),
    path('scorecard/', scorecard, name='scorecard'),
    path('my-page/', my_page, name='my-page'),
    path("players/", PlayersListView.as_view(), name="players"),
    path("players/<pk>", PlayersDetailView.as_view(), name="players"),

    path("putting_league/", PuttingLeagueListView.as_view(), name="putting_league"),
    path("putting_league/<pk>", PuttingLeagueDetailView.as_view(), name="putting_league"),
    path('standings/', StandingsAPIView.as_view(), name='standings'),
]
