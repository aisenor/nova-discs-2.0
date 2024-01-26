from django.urls import path
from django.contrib import admin
from api.views import home

from api.players.list_view import PlayersListView
from api.players.detail_view import PlayersDetailView
from api.putting_league.list_view import PuttingLeagueListView
from api.putting_league.detail_view import PuttingLeagueDetailView
from api.standings.list_view import StandingsAPIView

urlpatterns = [
    path('', home, name='home'),
    path('/', home, name='home'),
    path('admin/', admin.site.urls),
    path("players/", PlayersListView.as_view(), name="players"),
    path("players/<pk>", PlayersDetailView.as_view(), name="players"),

    path("putting_league/", PuttingLeagueListView.as_view(), name="putting_league"),
    path("putting_league/<pk>", PuttingLeagueDetailView.as_view(), name="putting_league"),
    path("putting_league/<int:player_id>", PuttingLeagueListView.as_view(), name="putting_league"),
    path('standings/', StandingsAPIView.as_view(), name='standings'),
    path('my_scores/', PuttingLeagueListView.as_view(), name="putting_league")
]
