from django.contrib import admin

from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'email','nickname', 'birthday', 'gender', 'address', 'phone_num', 'image')
    search_fields = ('username', 'email','nickname', 'birthday', 'gender', 'address', 'phone_num')
    list_filter = ('username', 'email','nickname', 'address', 'phone_num')

admin.site.register(UserProfile, UserProfileAdmin)
# Register your models here.
