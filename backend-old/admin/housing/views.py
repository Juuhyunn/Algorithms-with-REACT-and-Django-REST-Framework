# from django.shortcuts import render
#
# # Create your views here.
# from rest_framework.decorators import api_view, parser_classes
# from rest_framework.parsers import JSONParser
# from rest_framework import status
# from django.http import JsonResponse
#
# from admin.housing.models import Housing
# from admin.housing.serializers import HousingSerializer
# from icecream import ic
#
#
# @api_view(['GET', 'POST'])
# @parser_classes([JSONParser])
# def housings(request):
#     if request.method == 'GET':
#         ic('**********GET')
#         all_housings = Housing.objects.all()
#         serializer = HousingSerializer(all_housings, many=True)
#         return JsonResponse(data=serializer, safe=False)
#     elif request.method == 'POST':
#         ic('**********POST')
#         new_housing = request.data['body']
#         ic(new_housing)
#         serializer = HousingSerializer(data= new_housing['housing'])
#         ic('**********')
#         ic(serializer)
#         ic('**********')
#
