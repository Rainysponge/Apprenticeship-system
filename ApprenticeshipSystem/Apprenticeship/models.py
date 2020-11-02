from django.db import models
from user.models import Profile
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.


# class Profile(models.Model):
#     user = models.OneToOneField(User)
#     is_teacher = models.BooleanField(default=False)
#     is_student = models.BooleanField(default=True)
# 可以用这种方式实现user类型的分类，而且在前端只要调用
# {% if user.is_teacher %}{% if user..is_student %}就可以区分身份
# 也赋予了user既是学生有时老师的可能  {% if user.is_student and user.is_teacher %}
# 但实现上还需要斟酌，或者对于三种用户分别编写页面
# 也可以使用AbstractUser(个人跟倾向于这个)


# class Major(models.Model):
#     major = models.CharField(max_length=10)
#
#     def __str__(self):
#         return self.major
#
#
# class Sex(models.Model):
#     sex = models.CharField(max_length=1)  # 怎么限制男女？？？
#
#     def __str__(self):
#         return self.sex


class Teacher(models.Model):
    teacher_name = models.CharField(max_length=10, null=True)
    teacher_No = models.ForeignKey(Profile, on_delete=models.DO_NOTHING, default='00000')

    enter_time = models.DateTimeField()
    grade = models.CharField(max_length=5)
    # major = models.ForeignKey(Major, on_delete=models.DO_NOTHING)
    skill = models.CharField(max_length=50)
    self_introduction = models.CharField(max_length=50)

    def __str__(self):
        return self.teacher_name


class Student(models.Model):
    student_No = models.ForeignKey(Profile, on_delete=models.DO_NOTHING, default='00000')
    student_name = models.CharField(max_length=10)
    # student_sex = models.ForeignKey(Sex, on_delete=models.DO_NOTHING)
    school = models.CharField(max_length=10)
    enter_time = models.DateTimeField()
    grade = models.CharField(max_length=5)
    # major = models.ForeignKey(Major, on_delete=models.DO_NOTHING, null=True)  # 为什么就这里会报错？？？
    help = models.CharField(max_length=50)
    self_introduction = models.CharField(max_length=50)

    def __str__(self):
        return self.student_name


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
