from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from .models import User
from .validators import validate_user_data
from .serializers import (
    UserSerializer,
)

class UserCreateView(APIView):

    def post(self, request):
        # 유효성 검사
        rlt_message = validate_user_data(request.data)
        if rlt_message is not None:
            return Response()

        # 사용자 생성 로직
        validate_user_data = {
            "user_id": request.data.get("user_id"),
            "name": request.data.get("name"),
            "password": request.data.get("password"),
            "bio": request.data.get("bio"),
            "profile_image": request.data.get("profile_image"),
            "phone_number": request.data.get("phone_number"),
            "email": request.data.get("email"),
        }

        # 사용자 생성
        user = User.objects.create_user(**validate_user_data)

        # 생성된 사용자 직렬화 후 반환
        serializer = UserSerializer(user)
        return Response(serializer.data, status=201)