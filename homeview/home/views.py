from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
import django_filters
from .serializers import *
from .filters import *
from rest_framework.generics import *
from rest_framework.views import *
from django.views.generic.edit import DeleteView
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.forms import UserCreationForm
from rest_framework import status
from django.contrib.auth.backends import *
from django.contrib.auth import authenticate
from rest_framework.parsers import JSONParser


search1 = ""

@api_view(['GET'])
def ApiOverview(request):
	api = {
		'plz work': 'No I wont',
	}
	return Response(api)


class ItemListView(ListAPIView):
    queryset = Item.objects.all().order_by('time')
    serializer_class = ItemSerializer
    #filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    #filterset_class = ItemFilter
    #ordering = ['time']

class create(CreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class new(RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer




class showlist(ListAPIView):
    queryset = Showsavailable.objects.all()
    serializer_class = ShowSerializer
     
class addshow(CreateAPIView):
    queryset = Showsavailable.objects.all()
    serializer_class = ShowSerializer

class reviewshow(RetrieveUpdateDestroyAPIView):
    queryset = Showsavailable.objects.all()
    serializer_class = ShowSerializer
     



class bookedshowlist(ListAPIView):
    queryset = BookedShows.objects.all()
    serializer_class = BookedShowSerializer
    

class bookedshowdelete(DestroyAPIView):
    queryset = BookedShows.objects.all()
    serializer_class = BookedShowSerializer


'''
@api_view(['POST'])
def Register(request):
 
    username=request.data.get("username")
    password=request.data.get("password")
    
    
    return JsonResponse({'token': str(refresh.access_token)})

'''

class UserRegistration(APIView):
    querySet = Registermodel.objects.all()
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        print(request.data)
        if serializer.is_valid():
            user = User.objects.create_user(username=serializer.validated_data['username'],
                                                password=serializer.validated_data['password'])
            refresh = RefreshToken.for_user(user)
            return Response({'token': str(refresh.access_token)}, status=status.HTTP_201_CREATED)
    
    '''
    user = User.objects.create_user(username=username, password=password)
    refresh = RefreshToken.for_user(user)
    
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.save()
        user = User.objects.create_user(username=username, password=password)
        refresh = RefreshToken.for_user(user)
    '''
'''
class userlogin(APIView):
    #querySet = Loginmodel.objects.all()
    serializer_class = LoginSerializer


    def post(self,request):
        
        serializer = LoginSerializer(data=request.data)
        print(request.data)
        print(serializer.is_valid())
        print(serializer.errors)
        if serializer.is_valid():
            username=request.data.get("username")
            password=request.data.get("password")
            user = authenticate(request, username=username, password=password)
            print(user)
            if user is not None:
                refresh = RefreshToken.for_user(user)
                print("Hi")
                return Response({'token': str(refresh.access_token)}, status=status.HTTP_200_OK)
            else:
                return Response({'issue':'invalid'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
'''

class userlogin(APIView):
    serializer_class = LoginSerializer

    def post(self, request):
        

        
            username = request.data.get("username")
            password = request.data.get("password")
            user = authenticate(request, username=username, password=password)

            if user is not None:
                # Authentication successful
                refresh = RefreshToken.for_user(user)
                return Response({'token': str(refresh.access_token)}, status=status.HTTP_200_OK)
            else:
                # Invalid credentials
                return Response({'error': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)
        

#{'csrfmiddlewaretoken': ['XB7ekVqayK1iIr9G87el5P1cM9AK3DcsVXN8jSBhpzDVI0Wb7p9XK6LkWOBEiO3Z'], 'username': ['kk'], 'password': ['user']}
            

class Find(ListAPIView):
    queryset = User.objects.all()
    serializer_class = LoginSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_class = SearchFilter