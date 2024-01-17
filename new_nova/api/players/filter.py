from django_filters import rest_framework as filters

from backend.models.players import Players


class PlayersFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='exact')

    class Meta:
        model = Players
        fields = ['name']
