from django.http import JsonResponse
from django.shortcuts import render

from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser

from admin.crawling.models import Crawling, NewsCrawling


@api_view(['GET', 'POST'])
@parser_classes([JSONParser])
def process(request):
    Crawling().process()
    return JsonResponse({'Crawling': 'SUCCESS'})

@api_view(['GET', 'POST'])
@parser_classes([JSONParser])
def process(request):
    NewsCrawling().process()
    return JsonResponse({'NewsCrawling': 'SUCCESS'})