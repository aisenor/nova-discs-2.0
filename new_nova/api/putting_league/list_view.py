from rest_framework.generics import ListCreateAPIView
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .serializer import PuttingLeagueSerializer
from .filter import PuttingLeagueFilter
from backend.models.putting_league import PuttingLeague

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
@method_decorator(
    name="post",
    decorator=swagger_auto_schema(
        operation_summary="POST /putting_league/",
        operation_description=""
    )
)
class PuttingLeagueListView(ListCreateAPIView):
    serializer_class = PuttingLeagueSerializer
    queryset = PuttingLeague.objects.all()
    filterset_class = PuttingLeagueFilter
