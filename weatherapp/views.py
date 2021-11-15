from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from .serializers import UserSerializer
from .models import User
# Create your views here.

def index(request):
    return HttpResponse("Olá mundo! Este é o app notes de Tecnologias Web do Insper.")

@api_view(['GET', 'POST', 'DELETE'])
def api_user(request, username):
    if request.method == 'POST':
        new_user_data = request.data
        try:
            user = User.objects.get(username=username)
            user.cities = new_user_data['cities']
            print("try")
        except:
            user = User(username=username, cities=new_user_data['cities'])
            print("except")
        user.save()
    else:
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise Http404()
    
    serialized_user = UserSerializer(user)
    return Response(serialized_user.data)