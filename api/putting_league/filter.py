from django_filters import rest_framework as filters

from backend.models.putting_league import PuttingLeague


class PuttingLeagueFilter(filters.FilterSet):
    date = filters.CharFilter(lookup_expr='exact')
    player = filters.NumberFilter(lookup_expr='exact')
    score = filters.NumberFilter(lookup_expr='exact')

    class Meta:
        model = PuttingLeague
        fields = ['date', 'player', 'score']
