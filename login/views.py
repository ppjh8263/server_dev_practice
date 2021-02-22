from rest_framework.views import APIView
from rest_framework.response import Response
from .models import LoginUser
from django.contrib.auth.hashers import  make_password,check_password

# Create your views here.

class AppLogin(APIView):
    def post(self, request):
        user_id = request.data.get('user_id')
        user_pw = request.data.get('user_pw')

        user = LoginUser.objects.filter(user_id=user_id).first()

        if user is None:
            return Response(dict(msg="해당 사용자가 없습니다."))

        if check_password(user_pw, user.user_pw):
            return Response(dict(msg="로그인 성공"))
        else:
            return Response(dict(msg="로그인 실패, 비밀번호 틀림!"))


class RegistUser(APIView):
    def post(self, request):
        user_id = request.data.get('user_id')
        user_pw = request.data.get('user_pw')
        user_pw_encryted = make_password(user_pw)

        # if user_id = 특수문자, 숫자, 한글

        user = LoginUser.objects.filter(user_id=user_id).first()



        if user is not None:
            return Response(dict(msg="동일한 ID가 있습니다."))

        LoginUser.objects.create(user_id=user_id,
                                 user_pw=user_pw_encryted)

        data = dict(
            user_id=user_id,
            user_pw=user_pw_encryted
        )

        return Response(data)
