from .models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "user_id",
            "name",
            "job",
            "bio",
            "workplace",
            "profile_image",
            "employment_type",
            "email",
            "phone_number",
        ]

class UserProfileSerializer(serializers.ModelSerializer):
    following_count = serializers.SerializerMethodField()
    follow_count = serializers.SerializerMethodField()

    def get_following_count(self, obj):
        return obj.followings.count()
    
    def get_follow_count(self, obj):
        return obj.follow.count()

    class Meta:
        model = User
        fields = [
            "profile_image"
            "user_id",
            "name",
            "job",
            "bio",
            "workplace",
            "employment_type",
            "email",
            "phone_number",
            "following_count",
            "follow_count",
        ]

class MyProfileSerializer(serializers.ModelSerializer):
    
    follow_count = serializers.SerializerMethodField
    following_count = serializers.SerializerMethodField
    
    def get_follower_count(self, obj):
        return obj.following.count()
    
    def get_follow_count(self, obj):
        return obj.follow.count()
    
    class Meta:
        model = User
        fields = [
            "profile_image"
            "user_id",
            "name",
            "job",
            "bio",
            "workplace",
            "employment_type",
            "email",
            "phone_number",
            "following_count",
            "follow_count",
        ]