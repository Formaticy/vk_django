from rest_framework.serializers import ModelSerializer
from .models import Users, Friends, Statuses


class UsersSerializer(ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'


class FriendsRequestSerializer(ModelSerializer):
    class Meta:
        model = Friends
        fields = ('friend_one', 'friend_two')


class FriendsResponseSerializer(ModelSerializer):
    class Meta:
        model = Friends
        fields = '__all__'


class StatusesSerializer(ModelSerializer):
    class Meta:
        model = Statuses
        fields = '__all__'
