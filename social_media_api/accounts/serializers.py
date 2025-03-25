from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

# User Registration Serializer
class UserRegistrationSerializer(serializers.Serializer):
    password = serializers.CharField()

    class Meta:
        model = get_user_model()
        fields = ['id', 'email', 'password', 'bio', 'profile_picture']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = get_user_model().objects.create_user(**validated_data, password=password)
        Token.objects.create(user=user)
        return user

# User Login Serializer
class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)  
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        
        # Authenticate user
        user = authenticate(username=email, password=password)
        if user and user.is_active:
            token, _ = Token.objects.get_or_create(user=user)
            return {
                'user': user,
                'token': token.key
            }
        raise serializers.ValidationError("Invalid Credentials")
