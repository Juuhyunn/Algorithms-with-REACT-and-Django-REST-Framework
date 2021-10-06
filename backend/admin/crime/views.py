from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser

from admin.crime.models import CrimeCctvMode


@api_view(['GET'])
@parser_classes([JSONParser])
def crimes(request):
    CrimeCctvMode().create_crime_model()
    return JsonResponse({'crime': 'SUCCESS'})
