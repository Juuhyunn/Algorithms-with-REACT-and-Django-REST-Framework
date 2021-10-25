from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser

from admin.myNLP.models import Imdb, NaverMovie


@api_view(['GET', 'POST'])
@parser_classes([JSONParser])
def imdb_process(request):
    Imdb().imdb_process()
    return JsonResponse({'NIP imdb_process': 'SUCCESS'})


@api_view(['GET', 'POST'])
@parser_classes([JSONParser])
def naver_process(request):
    NaverMovie().naver_process()
    return JsonResponse({'NIP naver_process': 'SUCCESS'})