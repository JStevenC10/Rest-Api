from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.urls import path

from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.generics import CreateAPIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .serializers import UserSerializer

# REGISTER USER FOR API
class RegisterView(CreateAPIView):
    serializer_class = UserSerializer
    token_serializer = TokenObtainPairSerializer # SERIALIZER FOR TOKEN TO NEW USER
    permission_classes = [AllowAny]
    
    def create(self, request, *args, **kwargs):
        user = self.serializer_class(data=request.data)
        if user.is_valid():
            user.save()
            # USE THIS DICT FOR OBTAIN TOKEN TO NEW USER
            data_for_token = {
                "username": user.validated_data['username'],
                "password": user.validated_data['password']
            }
            login_serializer = self.token_serializer(data=data_for_token)
            if login_serializer.is_valid():
                return Response(
                            {
                                'user': user.validated_data['username'],
                                'message': 'Welcome to the API',
                                'token': login_serializer.validated_data['access'],
                                'refresh': login_serializer.validated_data['refresh'],
                            }, status=status.HTTP_201_CREATED
                        )
            else:
                return Response(login_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)      
    

# CLASS REDEFINED FOR RESPONSE MIXINS
class LoginView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        try:
            username = request.data['username']
            password = request.data['password']
            user = authenticate(username=username, password=password)
            if user:
                login_serializer = self.serializer_class(data=request.data)
                if login_serializer.is_valid():
                    return Response(
                        {
                            'user': username,
                            'message': 'login success',
                            'token': login_serializer.validated_data['access'],
                            'refresh': login_serializer.validated_data['refresh']
                        }, status=status.HTTP_200_OK
                    )
                else:
                    return Response(login_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'message': 'Username or password invalid!'}, status=status.HTTP_400_BAD_REQUEST)
        except:
            pass

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('token/', LoginView.as_view(), name='login'),
    path('refresh/token/', TokenRefreshView.as_view(), name='refresh'),
]