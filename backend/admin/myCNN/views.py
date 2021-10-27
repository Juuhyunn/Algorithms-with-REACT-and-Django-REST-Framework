from django.http import JsonResponse
from django.shortcuts import render

from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser

from admin.myCNN.models import CatDogClassification, Cifar10Classification


@api_view(['GET', 'POST'])
@parser_classes([JSONParser])
def catdog_process(request):
    CatDogClassification().process()
    return JsonResponse({'CatDogClassification': 'SUCCESS'})


@api_view(['GET', 'POST'])
@parser_classes([JSONParser])
def cifa_process(request):
    Cifar10Classification().process()
    return JsonResponse({'Cifar10Classification': 'SUCCESS'})

