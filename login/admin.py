from django.contrib import admin

# Register your models here.
from .models import LoginUser

admin.site.register(LoginUser)