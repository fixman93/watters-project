from django.contrib import admin
from custom_user.admin import EmailUserAdmin
from .models import User


class UserAdmin(EmailUserAdmin):
    pass

admin.site.register(User, UserAdmin)
