from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

class User(AbstractUser):
    name = models.CharField(max_length=20)
    job = models.CharField(max_legnth=20)
    bio = models.TextField(null=True, blank=True) # 공백이어도 상관없음.
    profile_image = models.ImageField(
        upload_to="user/image/%Y/%m/%d/", null=True, blank=True
    )
    workplace = models.CharField()
    employment_type = models.CharField()
    email = models.EmailField()
    phone_number = models.CharField(
        max_length=13,
        blank=True,
        null=True,
        unique=True,
        validators=[RegexValidator(r"010-?[1-9]\d{3}-\d{4}")],
    )
    created_at = models.DateTimeField(auto_now_add=True)

    followings = models.ManyToManyField( # ManytoManyField는 대칭적 관계이다.
        "self", symmetrical=False, related_name = "followers", blank=True
    ) # "self" : 사용자와 사용자 간의 관계 설정, symmetrical=False : 비대칭적 관계로 변경, related_name = "followers" : 반대 방향에서 참고할 때, 사용할 이름을 정의
    def __str__(self):
        return self.username