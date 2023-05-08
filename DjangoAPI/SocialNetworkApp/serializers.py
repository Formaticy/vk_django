from rest_framework.serializers import ModelSerializer
from .models import Users, Friends, Statuses


class UserSerializer(ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'


class FriendsSerializer(ModelSerializer):
    class Meta:
        model = Friends
        fields = '__all__'


class StatusesSerializer(ModelSerializer):
    class Meta:
        model = Statuses
        fields = '__all__'
