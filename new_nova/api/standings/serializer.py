from rest_framework import serializers


class StandingsSerializer(serializers.Serializer):
    top_3_daily = serializers.DictField(
        child=serializers.ListField(
            child=serializers.ListField(
                child=serializers.IntegerField()
            )
        )
    )
    top_5 = serializers.ListField(
        child=serializers.ListField(
            child=serializers.IntegerField()
        )
    )
