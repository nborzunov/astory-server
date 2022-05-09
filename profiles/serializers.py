from rest_framework import serializers
from .models import Profile, Follower


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('username', 'displayName', 'description', 'photoSrc', 'date_joined')



class UserByFollowerSerializer(serializers.ModelSerializer):
    photoSrc = serializers.ImageField(read_only=True)


class ListFollowerSerializer(serializers.ModelSerializer):
    subscribers = UserByFollowerSerializer(many=True, read_only=True)

    class Meta:
        model = Follower
        fields = ('subscribers',)
