from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser

from admin.ai_trader.models import AiTrader


@api_view(['GET', 'POST'])
@parser_classes([JSONParser])
def process(request):
    AiTrader().process()
    return JsonResponse({'AiTrader process': 'SUCCESS'})