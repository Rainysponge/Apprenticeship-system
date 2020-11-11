from django.db import models
from django.contrib.auth.models import User
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from ckeditor_uploader.fields import RichTextUploadingField
from .tools import user_directory_path


class Major(models.Model):
    major = models.CharField(max_length=10)

    def __str__(self):
        return self.major


class Sex(models.Model):
    sex = models.CharField(max_length=1)

    def __str__(self):
        return self.sex


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_ID = models.CharField(max_length=8, null=True, verbose_name="学号")
    portrait = models.ImageField('头像', upload_to=user_directory_path, blank=True, null=True)
    real_name = models.CharField(max_length=10, null=True, verbose_name="真实姓名")
    nickname = models.CharField(max_length=20, verbose_name='昵称')
    school = models.CharField(max_length=10, default='华东理工大学')
    sex = models.CharField(max_length=2, null=True)
    grade = models.CharField(max_length=5)
    major = models.ForeignKey(Major, on_delete=models.DO_NOTHING, null=True)
    photo_resize = ImageSpecField(  # 注意：ImageSpecField 不会生成数据库表的字段
        source='portrait',
        processors=[ResizeToFill(148, 207)],  # 处理成一寸照片的大小
        format='JPEG',  # 处理后的图片格式
        options={'quality': 95}  # 处理后的图片质量
    )

    def photo_resize_url(self):
        if self.photo_resize and hasattr(self.photo_resize, 'url'):
            return self.photo_resize.url
        else:
            return '\\media\\upload\\default\\user.jpg'

    def __str__(self):
        return '<Profile: %s for %s>' % (self.nickname, self.user.username)

    def photo_url(self):
        if self.portrait and hasattr(self.portrait, 'url'):
            return self.portrait.url
        else:
            return '\\media\\upload\\default\\user.jpg'


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    teacher_name = models.CharField(max_length=10, null=True)
    skill = models.CharField(max_length=50, null=True)
    enter_time = models.DateTimeField(null=True, blank=True)
    self_introduction = RichTextUploadingField(null=True)

    def __str__(self):
        if self.teacher_name:
            return self.teacher_name
        else:
            return '未知'


def get_teacher(self):
    if Teacher.objects.filter(user=self).exists():
        teacher = Teacher.objects.get(user=self)
        return teacher
    else:
        return ''


User.teacher = get_teacher


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    student_name = models.CharField(max_length=10, null=True)

    enter_time = models.DateTimeField(null=True, blank=True)

    help = models.CharField(max_length=50, null=True)
    self_introduction = RichTextUploadingField(null=True)

    def __str__(self):
        if self.student_name:
            return self.student_name
        else:
            return '未知'


class ReadNum(models.Model):
    read_num = models.IntegerField(default=0)
    teacher = models.OneToOneField(Teacher, on_delete=models.DO_NOTHING)

    def __str__(self):
        return 'abc'


def get_school(self):
    if Profile.objects.filter(user=self).exists():
        profile = Profile.objects.get(user=self)
        return profile.school
    else:
        return ''


def get_Profile(self):
    if Profile.objects.filter(user=self).exists():
        profile = Profile.objects.get(user=self)
        return profile
    else:
        return ''


User.get_school = get_school

User.Profile = get_Profile
