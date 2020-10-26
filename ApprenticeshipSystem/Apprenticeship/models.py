from django.db import models
from django.contrib.auth.models import User

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
