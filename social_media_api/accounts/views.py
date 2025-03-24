from django.shortcuts import render
from rest_framework import generics, status
from .models import CustomUser
from .serializers import UserRegistrationSerializer, UserLoginSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

# Create your views here.
class UserRegistrationView(generics.CreateAPIView):
     permission_classes = [AllowAny]
     queryset = CustomUser.objects.all()
     serializer_class = UserRegistrationSerializer
     
class UserLoginView(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                "token": token.key,
                "user": {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                    "bio": user.bio
                }
            })
        raise Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)