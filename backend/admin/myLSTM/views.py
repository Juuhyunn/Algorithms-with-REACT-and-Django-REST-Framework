from django.http import JsonResponse
from django.shortcuts import render

from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser

from admin.myLSTM.models import Trader


@api_view(['GET', 'POST'])
@parser_classes([JSONParser])
def process(request):
    Trader().process()
    return JsonResponse({'Trader': 'SUCCESS'})

# Create your views here.
