from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models

class UserProfile(AbstractUser):
    nickname = models.CharField(max_length=16, verbose_name="昵称", default=" ")
    birthday = models.DateTimeField(verbose_name="出生日期", null=True, blank=True)
    gender = models.CharField(max_length=8, choices=(("male","先生"), ("female","女士")), default="male",verbose_name="性别")
    address = models.CharField(max_length=32, verbose_name="地址",default=" ", null=True, blank=True)
    phone_num = models.CharField(max_length=11, verbose_name="手机号码")
    image = models.ImageField(upload_to="image/%Y/%m", default="image/default.png", max_length=128, verbose_name="用户头像")

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name


class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=8, verbose_name="验证码")
    email = models.CharField(max_length=32, verbose_name="邮箱")
    send_type = models.CharField(max_length=8, choices=(("register","注册"), ("forget password","忘记密码")), default="register", verbose_name="验证类型")
    send_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = "邮箱验证码"
        verbose_name_plural = verbose_name


class Banner(models.Model):
    title = models.CharField(max_length=20, verbose_name="标题")
    image = models.ImageField(upload_to="image/%Y/%m", default="image/default.png", max_length=128, verbose_name="封面图")
    url = models.URLField(max_length=200, verbose_name="访问地址")
    index = models.IntegerField(default=100, verbose_name="顺序")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "轮播图"
        verbose_name_plural = verbose_name