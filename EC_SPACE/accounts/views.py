from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from .validators import validate_user_data
from .serializers import (
    UserSerializer,
    UserProfileSerializer,
    MyProfileSerializer,
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
        serializer = UserSerializer(user) # 사용자 정보를 직렬화하여 JSON 데이터 형식으로 반환
        return Response(serializer.data, status=201)

class UserLoginView(APIView):

    def post(self, request):
        username=request.data.get("username")
        password=request.data.get("password")

        user = authenticate(username=username, password=password)
        if not user:
            return Response(
                {"message": "아이디 또는 비밀번호가 틀렸습니다"}, status=400 
            )
        
        refresh = RefreshToken.for_user(user)
        
        serializer = UserSerializer(user)
        
        return Response(
            {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "user_info": serializer.data,
            }
        )

class UserProfileView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, user_id):
        # 특정 사용자의 프로필 조희
        user=get_object_or_404(User, user_id=user_id)

        if request.user == user:
            serializer = UserProfileSerializer(user)
            return Response(serializer.data)
        else:
        # 현재 로그인한 사용자 프로필 조회
            serializer = MyProfileSerializer(user)
            return Response(serializer.data)