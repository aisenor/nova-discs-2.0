from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .serializer import PlayersSerializer
from .filter import PlayersFilter
from backend.models.players import Players

@method_decorator(
    name="get",
    decorator=swagger_auto_schema(
        operation_summary="",
        operation_description="",
        manual_parameters=[
            openapi.Parameter(
                name="data",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                required=False
            ),
            openapi.Parameter(
                name="player",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                required=False
            ),
            openapi.Parameter(
                name="score",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                required=False
            ),
        ]
    )
)
class PlayersListView(ListCreateAPIView):
    serializer_class = PlayersSerializer
    queryset = Players.objects.all()
    filterset_class = PlayersFilter

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({'players': serializer.data})
