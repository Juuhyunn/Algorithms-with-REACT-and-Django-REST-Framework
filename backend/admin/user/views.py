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
        return JsonResponse(data = serializer.data, safe = False)
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
        ic(request)
        edit_user = request.data
        ic(edit_user)
        # serializer = UserSerializer(data = new_user['user'])
        dbUser = UserVo.objects.get(pk=edit_user['username'])
        print(f'{type(dbUser)}')  # <class 'admin.user.models.User'>
        ic(f'변경 전 : {dbUser}')
        # for i in edit_user.keys():
        #     dbUser.i = edit_user[i]
        #     # dbUser.save()
        #     print(i + ": " + dbUser.i)
        dbUser.name = edit_user["name"]
        dbUser.email = edit_user["email"]
        dbUser.password = edit_user["password"]
        dbUser.birth = edit_user["birth"]
        dbUser.address = edit_user["address"]
        ic(f'변경 후 : {dbUser}')
        dbUser.save()
        userSerializer = UserSerializer(dbUser, many=False)
        return JsonResponse(data=userSerializer.data, safe=False)

#
# @api_view(['GET','POST'])
# @parser_classes([JSONParser])
# def users(request, id):
#     pass


@api_view(['POST'])
def login(request):
    try:
        loginUser = request.data
        # print(f'{type(loginUser)}') # <class 'dict'>
        ic(loginUser)
        dbUser = UserVo.objects.get(pk = loginUser['username'])
        print(f'{type(dbUser)}') # <class 'admin.user.models.User'>
        ic(dbUser)
        if loginUser['password'] == dbUser.password:
            print('******** 로그인 성공')
            userSerializer = UserSerializer(dbUser, many=False)
            ic(userSerializer)
            return JsonResponse(data=userSerializer.data, safe=False)
        else:
            print('******** 비밀번호 오류')
            return JsonResponse(data={'result':'PASSWORD-FAIL'}, status=201)

    except UserVo.DoesNotExist:
        print('*' * 50)
        print('******** Username 오류')
        return JsonResponse(data={'result':'USERNAME-FAIL'}, status=201)


@api_view(['DELETE'])
def remove(request, username):
    ic('**********DELETE')
    ic(request)
    del_user = request.data
    ic(username)
    ic(type(username))
    dbUser = UserVo.objects.get(pk=username)
    dbUser.delete()
    return JsonResponse(data = {'result':'Delete Success'}, status=201)

@api_view(['POST'])
@parser_classes([JSONParser])
def detail(request):
    ic('**********Detail')
    detailUser = request.data
    # print(f'{type(loginUser)}') # <class 'dict'>
    ic(detailUser)
    dbUser = UserVo.objects.get(pk=detailUser['username'])
    print(f'{type(dbUser)}')  # <class 'admin.user.models.User'>
    ic(dbUser)
    userSerializer = UserSerializer(dbUser, many=False)
    return JsonResponse(data=userSerializer.data, safe=False)

