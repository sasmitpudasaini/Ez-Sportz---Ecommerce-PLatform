from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# This makes your CustomUser visible in the Django Admin panel
admin.site.register(CustomUser, UserAdmin)