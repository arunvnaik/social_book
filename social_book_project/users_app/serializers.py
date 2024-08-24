from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers
from .models import UploadedFile

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True, label="Confirm Password")

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password']
        extra_kwargs = {
            'password': {'write_only': True, 'min_length': 8},
        }

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError({"confirm_password": "Passwords must match."})
        
        
        # Check if the email is already registered
        # if User.objects.filter(email=data['email']).exists():
        #     raise serializers.ValidationError({"email": "A user with this email already exists."})
        
        return data
    
        
    
    
    def create(self, validated_data):
        # Remove confirm_password from validated_data since it's not needed for user creation
        validated_data.pop('confirm_password')
        
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise serializers.ValidationError("Invalid credentials provided.")
        else:
            raise serializers.ValidationError("Both 'username' and 'password' are required.")

        attrs['user'] = user
        return attrs

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'age', 'address', 'public_visibility'] 
        
class UploadedFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedFile
        fields = ['id', 'title', 'description', 'file', 'visibility', 'cost', 'year_of_published', 'uploaded_at']