from django.conf.urls import url
from .views import RegistUser

urlptterns = [
    url('regist_user', RegistUser.as_view(), name='regist_user')
]