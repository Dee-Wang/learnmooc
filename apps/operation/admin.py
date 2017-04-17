from django.contrib import admin

from .models import UserWant, CourseComments, UserCourse, UserFavor, UserMessage

class UserWantAdmin(admin.ModelAdmin):
    pass


class CourseCommentsAdmin(admin.ModelAdmin):
    pass


class UserCourseAdmin(admin.ModelAdmin):
    pass


class UserFavorAdmin(admin.ModelAdmin):
    pass


class UserMessageAdmin(admin.ModelAdmin):
    pass


admin.site.register(UserWant, UserWantAdmin )
admin.site.register(CourseComments, CourseCommentsAdmin )
admin.site.register(UserCourse, UserCourseAdmin )
admin.site.register(UserFavor, UserFavorAdmin )
admin.site.register(UserMessage, UserMessageAdmin )

# Register your models here.
