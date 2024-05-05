from rest_framework import serializers
from .models import Product, ProductImage, Category
from django.contrib.auth.models import User


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
        fields = ["name", "slug"]




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {"write_only": True}}


    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user





