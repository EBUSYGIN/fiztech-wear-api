from rest_framework import serializers
from .models import Product, ProductImage, Category
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, RefreshToken


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ["image", "alt_text"]





class ProductSerializer(serializers.ModelSerializer):
    product_image = ImageSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = ['id', 'title', 'category', 'description', 'slug', 'regular_price', 'product_image']




class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name", "slug", "id"]




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {"write_only": True}}


    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        # refresh = RefreshToken.for_user(user)
        # return user, refresh
        return user
    



    



class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    class Meta:
        model = User


    def validate(self, attrs):
        user = User.objects.filter(username = attrs['username']).first()
        if user is None:
            raise serializers.ValidationError('Неверное имя пользователя или пароль.')

        if not user.check_password(attrs.get('password')):
            raise serializers.ValidationError('Неверное имя пользователя или пароль.')
        
        # user_serializer = UserSerializer(user)
        refresh = self.get_token(user)
        data = {}
        data['id'] = str(UserSerializer(user).data['id'])
        data['username'] = str(UserSerializer(user).data['username'])
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        return data
        # user_serializer.data, 


# class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
#     def validate(self, attrs):
#         user = User.objects.filter(username=attrs.get('username')).first()

        # if user is None:
        #     raise serializers.ValidationError('Неверное имя пользователя или пароль.')

        # if not user.check_password(attrs.get('password')):
        #     raise serializers.ValidationError('Неверное имя пользователя или пароль.')
        
#         refresh = self.get_token(user)

#         data = {}
#         data['refresh'] = str(refresh)
#         data['access'] = str(refresh.access_token)

#         return data




