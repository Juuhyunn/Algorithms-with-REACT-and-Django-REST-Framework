from django.http import JsonResponse
from django.shortcuts import render

from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser

from admin.tensor.models import Calculator


@api_view(['GET', 'POST'])
@parser_classes([JSONParser])
def calculator(request):
    Calculator().process()
    return JsonResponse({'Calculator': 'SUCCESS'})