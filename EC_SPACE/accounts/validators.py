from .models import User
import re

def validate_user_data(user_data):
    user_id = user_data.get("user_id")
    name = user_data.get("name")
    job = user_data.get("job")
    password = user_data.get("password")
    bio = user_data.get("bio")
    profile_image = user_data.get("profile_image")
    phone_number = user_data.get("phone_number")
    workplace = user_data.get("workplace")
    email = user_data.get("email")

    error_message = []

    if len(name) > 20:
        error_message.append("이름은 20자 미만이어야 합니다.")

    if len(job) > 20:
        error_message.append("직업명은 20자 미만이어야 합니다.")

    if len(password) <= 8:
        error_message.append("비밀번호는 8글자 이상이어야 합니다.")

    if User.objects.filter(user_id=user_id).exists():
        error_message.append("이미 존재하는 아이디입니다.")

    if email:
        pattern = r"^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if not re.match(pattern, email):
            error_message.append("유효하지 않은 이메일입니다.")
        
        if User.objects.filter(email=email).exists():
            error_message.append("이미 존재하는 이메일입니다.")

    if not name:
        error_message.append("이름은 필수 등록 사항입니다.")

    if phone_number:
        pattern = r"010-?[1-9]\d{3}-\d{4}" # 010-****-**** 형식의 정규 코드식
        if not re.match(pattern, phone_number):
            error_message.append("전화번호는 010-****-**** 형식으로 입력해주세요.")

        if User.objects.filter(phone_number=phone_number).exists():
            error_message.append("이미 존재하는 전화번호입니다.")

    if error_message:
        return error_message
    return None