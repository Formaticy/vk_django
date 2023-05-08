from django.db import models


# Create your models here.

class Users(models.Model):
    userId = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, unique=True)


class Statuses(models.Model):
    statusId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)


class Friends(models.Model):
    friendId = models.AutoField(primary_key=True)
    friend_one = models.ForeignKey(Users, on_delete=models.CASCADE)
    friend_two = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='friend_set')
    statusId = models.ForeignKey(Statuses, on_delete=models.SET_NULL, null=True)

    class Meta:
        unique_together = (('friend_one', 'friend_two'),)
