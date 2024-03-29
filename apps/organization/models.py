from datetime import datetime

from django.db import models


class CityDict(models.Model):
    name = models.CharField(max_length=8, verbose_name="城市名")
    description = models.CharField(max_length=32, verbose_name="城市简述")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "城市信息"
        verbose_name_plural = verbose_name


class CourseOrg(models.Model):
    city = models.ForeignKey(CityDict, verbose_name="所在城市")
    name = models.CharField(max_length=16, verbose_name="课程机构名")
    description = models.CharField(max_length=32, verbose_name="机构简述")
    favor_num = models.IntegerField(default=0, verbose_name="收藏人数")
    click_num = models.IntegerField(default=0, verbose_name="点击量")
    address = models.CharField(max_length=64, verbose_name="机构地址")
    phone_num = models.CharField(max_length=16, verbose_name="联系方式")
    image = models.ImageField(upload_to="organization/%Y/%m", default="organization/default.png", max_length=128, verbose_name="机构封面图")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "课程机构"
        verbose_name_plural = verbose_name


class Teacher(models.Model):
    organization = models.ForeignKey(CourseOrg, verbose_name="所属机构")
    name = models.CharField(max_length=16, verbose_name="讲师名")
    work_years = models.IntegerField(default=0, verbose_name="工作年限")
    work_company = models.CharField(max_length=32, verbose_name="供职单位", null=True, blank=True)
    work_position = models.CharField(max_length=16, verbose_name="公司职位", null=True, blank=True)
    characters = models.TextField(verbose_name="讲师风格", null=True, blank=True)
    favor_num = models.IntegerField(default=0, verbose_name="收藏人数")
    click_num = models.IntegerField(default=0, verbose_name="点击量")
    phone_num = models.CharField(max_length=16, verbose_name="联系方式")
    image = models.ImageField(upload_to="organization/teahers/%Y/%m", default="organization/teachers/default.png", max_length=128,
                              verbose_name="讲师照片")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "讲师信息"
        verbose_name_plural = verbose_name
