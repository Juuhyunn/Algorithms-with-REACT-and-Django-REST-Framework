from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser

from admin.myCV2.models import MyCV2


@api_view(['GET', 'POST'])
@parser_classes([JSONParser])
def lena(request):
    MyCV2().lena()
    return JsonResponse({'MyCV2 Lena': 'SUCCESS'})


@api_view(['GET', 'POST'])
@parser_classes([JSONParser])
def girl(request):
    MyCV2().girl()
    return JsonResponse({'MyCV2 girl': 'SUCCESS'})


@api_view(['GET', 'POST'])
@parser_classes([JSONParser])
def face_detect(request):
    MyCV2().face_detect()
    return JsonResponse({'MyCV2 face_detect': 'SUCCESS'})