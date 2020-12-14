from django.db import models
from user.models import Teacher, Student
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.


class Relationship(models.Model):
    SID = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    TID = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '<Profile: %s for %s>' % (self.SID, self.TID)


class Homework(models.Model):
    relationship_id = models.ForeignKey(Relationship, on_delete=models.DO_NOTHING)
    content = models.CharField(max_length=100)

    def __str__(self):
        return self.content


class Critic(models.Model):
    homework_id = models.ForeignKey(Homework, on_delete=models.DO_NOTHING)
    content = models.CharField(max_length=100)

    def __str__(self):
        return self.content


class ApprenticeRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING)
    created_time = models.DateTimeField(auto_now_add=True)
    result = models.IntegerField(default=0)  # 0表示请求中，1表示请求成功，2表示请求失败

    def __str__(self):
        return '<Profile: %s for %s>' % (self.user, self.teacher)
