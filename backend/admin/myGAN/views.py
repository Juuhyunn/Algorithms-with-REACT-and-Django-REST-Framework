from django.http import JsonResponse
from django.shortcuts import render

from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser

from admin.myGAN.models import AutoencodersGans


@api_view(['GET', 'POST'])
@parser_classes([JSONParser])
def process(request):
    AutoencodersGans().process()
    return JsonResponse({'AutoencodersGans': 'SUCCESS'})

# Create your views here.
