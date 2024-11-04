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
