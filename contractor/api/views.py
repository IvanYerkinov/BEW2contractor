from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response

from clock.models import Clock
from .serializers import ClockSerializer

# Create your views here.


class ClockList(APIView):
    def get(self, request):
        pages = Clock.objects.all()[:20]
        data = ClockSerializer(pages, many=True).data
        return Response(data)


class ClockDetail(APIView):
    def get(self, request, id):
        page = get_object_or_404(Clock, id=id)
        data = ClockSerializer(page).data
        return Response(data)
