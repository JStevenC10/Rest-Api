from django.contrib.auth import authenticate
from django.urls import path

from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.response import Response


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
    path('token/', LoginView.as_view(), name='login'),
    path('refresh/token/', TokenRefreshView.as_view(), name='refresh'),
]