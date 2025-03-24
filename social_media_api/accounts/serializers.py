from rest_framework import serializers
from .models import CustomUser
from rest_framework.authentication import authenticate

#User registration serializer
class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'password', 'bio', 'profile_picture', ]

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = CustomUser.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user

#User login serializer  
class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        
        # Authenticate user
        user = authenticate(request=self.context.get('request'), username=email, password=password)
        if user and user.is_active:
            return user  

        raise serializers.ValidationError("Invalid Credentials")
