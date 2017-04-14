from datetime import datetime

from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=16, verbose_name="课程名")
    description = models.CharField(max_length=32, verbose_name="课程简述")
    detail = models.TextField(verbose_name="课程介绍")
    degree = models.CharField(max_length=10, choices=(("easy","初级"), ("nomal","中级"), ("tough","高级")), default="easy", verbose_name="难度")
    learning_time = models.IntegerField(default=0, verbose_name="课程时长(单位:分钟)")
    learning_num = models.IntegerField(default=0, verbose_name="学习人数")
    favor_num = models.IntegerField(default=0, verbose_name="收藏人数")
    click_num = models.IntegerField(default=0, verbose_name="点击量")
    image = models.ImageField(upload_to="image/%Y/%m", default="image/default.png", max_length=128, verbose_name="课程封面")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "课程信息"
        verbose_name_plural = verbose_name


class Lesson(models.Model):
    course = models.ForeignKey(Course, verbose_name="所属课程")
    name = models.CharField(max_length=16, verbose_name="章节名")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "章节信息"
        verbose_name_plural = verbose_name


class Video(models.Model):
    course = models.ForeignKey(Course, verbose_name="所属课程")
    lesson = models.ForeignKey(Lesson, verbose_name="所属章节")
    name = models.CharField(max_length=16, verbose_name="视频名称")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "视频信息"
        verbose_name_plural = verbose_name


class VideoResource(models.Model):
    course = models.ForeignKey(Course, verbose_name="所属课程")
    name = models.CharField(max_length=16, verbose_name="资源名称")
    download = models.FileField(upload_to="course/resource/%Y/%m", verbose_name="下载地址")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "课程资源"
        verbose_name_plural = verbose_name