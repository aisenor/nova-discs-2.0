from rest_framework import serializers


class StandingsSerializer(serializers.Serializer):
    date = serializers.DateField()
    player = serializers.IntegerField()
    total_score = serializers.IntegerField()
