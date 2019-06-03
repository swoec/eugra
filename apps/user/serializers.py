from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import UserProfile


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    username = serializers.CharField(max_length=30, label='username', required=True, allow_blank=False,
                                     validators=[UniqueValidator(queryset=User.objects.all(), message="existed")])

    class Meta:
        model = UserProfile
        fields = '__all__'


class UserAddSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type': 'password'}, help_text='password', label='code',
                                     write_only=True)
    username = serializers.CharField(max_length=30, label='username', required=True, allow_blank=False,
                                     validators=[UniqueValidator(queryset=User.objects.all(), message="existed")])

    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = super(UserAddSerializer, self).create(validated_data=validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user