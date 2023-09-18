from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import filters, status, viewsets
from . models import UrlData
from . serializer import UrlDataSerializer

# Create your views here.

class UrlDataViewSets(viewsets.ModelViewSet):
    queryset = UrlData.objects.all()
    serializer_class = UrlDataSerializer
    http_method_names = ["get", "post", "put", "delete"]
    filterset_fields = ["url", "slug"]
    search_fields = ["url", "slug"]
    ordering_fields = ["url", "slug"]

    def perform_create(self, serializer):
        serializer.save(slug=''.join(random.choice(string.ascii_letters)
                           for x in range(10)))


