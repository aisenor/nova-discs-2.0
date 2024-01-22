from rest_framework.generics import RetrieveUpdateDestroyAPIView
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema

from .serializer import PuttingLeagueSerializer
from backend.models.putting_league import PuttingLeague

@method_decorator(
    name="get",
    decorator=swagger_auto_schema(
        operation_summary="Retrieve",
        operation_description=""
    )
)
class PuttingLeagueDetailView(RetrieveUpdateDestroyAPIView):
    http_method_names = ["get", "put", "delete"]
    serializer_class = PuttingLeagueSerializer
    queryset = PuttingLeague.objects.all()
