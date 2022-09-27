from rest_framework import serializers
from ads.models.ad import Ad
from users.models import User


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'


class AdListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ['pk', 'title', 'price', 'description', 'image']


class AdCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ['title', 'price', 'description', 'image']


class AdDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ['id']


class AdRetrieveSerializer(serializers.ModelSerializer):
    phone = serializers.SlugRelatedField(source='author', many=False, queryset=User.objects.all(), slug_field='phone')
    first_name = serializers.SlugRelatedField(source='author', many=False, queryset=User.objects.all(),
                                                     slug_field='first_name')
    last_name = serializers.SlugRelatedField(source='author', many=False, queryset=User.objects.all(),
                                                    slug_field='last_name')

    class Meta:
        model = Ad
        fields = ['pk',  'title', 'price', 'description', 'image', 'phone', 'first_name', 'last_name', 'author_id']
