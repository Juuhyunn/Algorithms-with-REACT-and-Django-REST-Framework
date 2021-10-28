from astroid.builder import objects
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser

from admin.user.models import UserVo
from admin.user.serializers import UserSerializer
from icecream import ic


@api_view(['GET', 'POST', 'PUT'])
@parser_classes([JSONParser])
def users(request):
    if request.method == 'GET':
        ic('**********GET')
        all_users = UserVo.objects.all()
        print(all_users)
        serializer = UserSerializer(all_users, many=True)
        ic(serializer.data)
        data = objects.serializer

        return JsonResponse(data = data, safe = False)
    elif request.method == 'POST':
        ic('**********POST')
        ic(request)
        # new_user = request.data['body']
        new_user = request.data
        ic(new_user)
        # serializer = UserSerializer(data = new_user['user'])
        serializer = UserSerializer(data = new_user)
        ic('***************************************************')
        ic(serializer)
        ic('***************************************************')
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'result' : f'Welcome, {serializer.data.get("name")}'}, status=201)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        ic('**********PUT')
        return None

#
# @api_view(['GET','POST'])
# @parser_classes([JSONParser])
# def users(request, id):
#     pass


@api_view(['GET','POST'])
@parser_classes([JSONParser])
def login(request):
    pass





