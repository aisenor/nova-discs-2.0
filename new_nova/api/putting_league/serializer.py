from rest_framework import serializers

from backend.models.putting_league import PuttingLeague


class PuttingLeagueSerializer(serializers.ModelSerializer):
    class Meta:
        model = PuttingLeague
        fields = (
            "id",
            "date",
            "player",
            "score"
        )
