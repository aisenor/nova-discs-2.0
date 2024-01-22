from rest_framework import serializers

from backend.models.players import Players


class PlayersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Players
        fields = (
            "id",
            "name"
        )
