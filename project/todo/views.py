from django.http import HttpResponseBadRequest, HttpResponse
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import MethodNotAllowed
from django_filters.rest_framework import DjangoFilterBackend
from django.http import JsonResponse
from todo import settings 
from todo.models import Read
from todo.serializers import ReadSerializer


class ReadViewSet(ModelViewSet):
    serializer_class = ReadSerializer
    model = Read
    queryset = Read.objects.all()
    filter_backends = (DjangoFilterBackend, )
    

def ping(request):
    return HttpResponse("pong")

def status(request): 
    return JsonResponse({
        "status": "ok",
        "environment": settings.MODE,
        "name": settings.SERVICE_NAME
    })
