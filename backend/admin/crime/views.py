from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser

from admin.crime.models import Crime
from admin.crime.models_old import CrimeCctvMode


@api_view(['GET', 'POST'])
@parser_classes([JSONParser])
def crimes(request):
    # CrimeCctvMode().create_crime_model()
    CrimeCctvMode().create_police_position()
    return JsonResponse({'crime': 'SUCCESS'})


@api_view(['GET'])
@parser_classes([JSONParser])
def cctvs(request):
    CrimeCctvMode().create_cctv_model()
    return JsonResponse({'cctv': 'SUCCESS'})


@api_view(['GET'])
@parser_classes([JSONParser])
def populations(request):
    CrimeCctvMode().create_population_model()
    return JsonResponse({'population': 'SUCCESS'})


@api_view(['GET'])
@parser_classes([JSONParser])
def merge_cctv_pop(request):
    CrimeCctvMode().merge_cctv_population()
    return JsonResponse({'MERGE_cctv_population': 'SUCCESS'})


@api_view(['GET'])
@parser_classes([JSONParser])
def merge_crime_cctv(request):
    CrimeCctvMode().merge_crime_cctv()
    return JsonResponse({'MERGE_crime_cctv': 'SUCCESS'})


@api_view(['GET'])
@parser_classes([JSONParser])
def process(request):
    Crime().process()
    return JsonResponse({'crime_process': 'SUCCESS'})
