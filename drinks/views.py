from .models import Drinks,Users
from .serializers import DrinkSerializer,UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET','POST'])
def drink_list(request,format=None):

    if request.method == 'GET':
        drinks = Drinks.objects.all()
        serializer=DrinkSerializer(drinks,many=True)
        return Response(serializer.data)
    
    if request.method =='POST':
        serializer=DrinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
@api_view(['GET','PUT','DELETE'])
def drink_detail(request,id,format=None):

    try:
        drink=Drinks.objects.get(pk=id)
    except Drinks.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if  request.method == 'GET':
        serializer = DrinkSerializer(drink)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer=DrinkSerializer(drink,data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET','POST'])
def users_list(request,format=None):
    if request.method == 'GET':
        users=Users.objects.all()
        serializer=UserSerializer(users,many=True)
        return Response(serializer.data)
    
    if request.method =='POST':
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
        
@api_view(['GET','PUT','DELETE'])
def users_detail(request,id,format=None):

    try:
        users=Users.objects.get(pk=id)
    except Users.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if  request.method == 'GET':
        serializer = UserSerializer(users)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer=UserSerializer(users,data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        users.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
