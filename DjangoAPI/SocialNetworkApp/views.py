from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from drf_spectacular.utils import extend_schema

from .models import Users, Friends, Statuses
from .serializers import UsersSerializer, FriendsRequestSerializer, FriendsResponseSerializer, StatusesSerializer


# Create your views here.
@extend_schema(request=UsersSerializer, responses=UsersSerializer)
class UsersList(APIView):
    def get(self, request):
        users = Users.objects.all()
        serializer = UsersSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UsersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(request=UsersSerializer, responses=UsersSerializer)
class UsersDetail(APIView):
    def get_object(self, username):
        try:
            return Users.objects.get(username=username)
        except Users.DoesNotExist:
            raise Http404

    def get(self, request, username):
        user = self.get_object(username)
        serializer = UsersSerializer(user)
        return Response(serializer.data)

    def put(self, request, username):
        user = self.get_object(username)
        serializer = UsersSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, username):
        user = self.get_object(username)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StatusesList(generics.ListCreateAPIView):
    queryset = Statuses.objects.all()
    serializer_class = StatusesSerializer


class StatusesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Statuses.objects.all()
    serializer_class = StatusesSerializer


@extend_schema(request=FriendsRequestSerializer, responses=FriendsResponseSerializer)
class FriendsList(APIView):
    def get(self, request):
        friends = Friends.objects.all()
        serializer = FriendsResponseSerializer(friends, many=True)
        return Response(serializer.data)

    def post(self, request):
        fr_one_id = request.data['friend_one']
        fr_two_id = request.data['friend_two']
        if fr_one_id != fr_two_id:
            friends_req_before = Friends.objects.filter(friend_one=fr_two_id, friend_two=fr_one_id)
            if len(friends_req_before) != 0:
                friends_req_before.update(statusId=Statuses(statusId=4))
                return Response('you are friends!', status=status.HTTP_201_CREATED)
            else:
                serializer_new = FriendsRequestSerializer(data=request.data)
                if serializer_new.is_valid():
                    serializer_new.save(statusId=Statuses(statusId=2))
                    return Response('proposal was sended', status=status.HTTP_201_CREATED)
                return Response('id must be unique', status=status.HTTP_400_BAD_REQUEST)
        return Response('id must be unique or correct', status=status.HTTP_400_BAD_REQUEST)


@extend_schema(request=FriendsRequestSerializer, responses=FriendsResponseSerializer)
class FriendsDelete(APIView):
    def put(self, request):
        fr_one_id = request.data['friend_one']
        fr_two_id = request.data['friend_two']
        find_these_friends_1 = Friends.objects.filter(friend_one=fr_one_id, friend_two=fr_two_id).values('statusId')
        find_these_friends_2 = Friends.objects.filter(friend_one=fr_two_id, friend_two=fr_one_id).values('statusId')
        if len(find_these_friends_1) != 0 and find_these_friends_1[0]['statusId'] == 4:
            Friends.objects.filter(friend_one=fr_one_id, friend_two=fr_two_id).update(friend_one=fr_two_id, friend_two=fr_one_id, statusId=Statuses(statusId=2))
            return Response(f'{fr_one_id} and {fr_two_id} are not friends now')
        if len(find_these_friends_2) != 0 and find_these_friends_2[0]['statusId'] == 4:
            Friends.objects.filter(friend_one=fr_two_id, friend_two=fr_one_id).update(statusId=Statuses(statusId=2))
            return Response(f'{fr_one_id} and {fr_two_id} are not friends now')
        return Response('they are not friends! choose another one', status=status.HTTP_400_BAD_REQUEST)


@extend_schema(request=FriendsRequestSerializer, responses=FriendsResponseSerializer)
class FriendsReject(APIView):
    def put(self, request):
        fr_one_id = request.data['friend_one']
        fr_two_id = request.data['friend_two']
        proposal = Friends.objects.filter(friend_one=fr_one_id, friend_two=fr_two_id).values('statusId')
        if len(proposal) != 0 and proposal[0]['statusId'] == 2:
            Friends.objects.filter(friend_one=fr_one_id, friend_two=fr_two_id).delete()
            return Response(f'{fr_two_id} rejected proposal from {fr_one_id}')
        return Response(f'{fr_one_id} did not send a proposal to {fr_two_id}', status=status.HTTP_400_BAD_REQUEST)

@extend_schema(request=FriendsRequestSerializer, responses=FriendsResponseSerializer)
class FriendsAccept(APIView):
    def put(self, request):
        fr_one_id = request.data['friend_one']
        fr_two_id = request.data['friend_two']
        proposal = Friends.objects.filter(friend_one=fr_one_id, friend_two=fr_two_id).values('statusId')
        if len(proposal) != 0 and proposal[0]['statusId'] == 2:
            Friends.objects.filter(friend_one=fr_one_id, friend_two=fr_two_id).update(
                statusId=Statuses(statusId=4))
            return Response(f'{fr_two_id} accepted proposal from {fr_one_id}')
        return Response(f'{fr_one_id} did not send a proposal to {fr_two_id}', status=status.HTTP_400_BAD_REQUEST)


@extend_schema(request=FriendsRequestSerializer, responses=FriendsResponseSerializer)
class FriendsOutcomingProposals(APIView):
    def get(self, request, friend_one_id):
        friends = Friends.objects.filter(friend_one=friend_one_id, statusId=2)
        serializer = FriendsRequestSerializer(friends, many=True)
        if serializer.data:
            return Response(serializer.data)
        if len(friends) == 0:
            return Response('outcoming proposals = 0')


@extend_schema(request=FriendsRequestSerializer, responses=FriendsResponseSerializer)
class FriendsIncomingProposals(APIView):
    def get(self, request, friend_one_id):
        friends = Friends.objects.filter(friend_two=friend_one_id, statusId=2)
        serializer = FriendsRequestSerializer(friends, many=True)
        if serializer.data:
            return Response(serializer.data)
        if len(friends) == 0:
            return Response('incoming proposals = 0')


@extend_schema(request=FriendsRequestSerializer, responses=FriendsResponseSerializer)
class FriendsAlreadyFriends(APIView):
    def get(self, request, friend_one_id):
        friends_proposal_sent_from_one = Friends.objects.filter(friend_one=friend_one_id, statusId=4)
        friends_proposal_sent_to_one = Friends.objects.filter(friend_two=friend_one_id, statusId=4)
        serializer_1 = FriendsRequestSerializer(friends_proposal_sent_from_one, many=True)
        serializer_2 = FriendsRequestSerializer(friends_proposal_sent_to_one, many=True)
        if serializer_1.data or serializer_2.data:
            return Response(serializer_1.data + serializer_2.data)
        if len(friends_proposal_sent_from_one) + len(friends_proposal_sent_to_one) == 0:
            return Response('friends amount = 0')


@extend_schema(request=FriendsRequestSerializer, responses=FriendsResponseSerializer)
class FriendsStatus(APIView):
    def get(self, request, friend_one_id, friend_two_id):
        friends_1 = Friends.objects.filter(friend_one=friend_one_id, friend_two=friend_two_id).values('statusId')
        friends_2 = Friends.objects.filter(friend_one=friend_two_id, friend_two=friend_one_id).values('statusId')
        if len(friends_1) != 0:
            status = friends_1[0]['statusId']
            if status == 2:
                return Response(f'{friend_one_id} SEND propoposal {friend_two_id}')
            else:
                return Response(f'{friend_one_id} and {friend_two_id} are FRIENDS')
        if len(friends_2) != 0:
            status = friends_2[0]['statusId']
            if status == 2:
                return Response(f'{friend_two_id} SEND propoposal {friend_one_id}')
            else:
                return Response(f'{friend_one_id} and {friend_two_id} are FRIENDS')
        else:
            return Response('nothing')
