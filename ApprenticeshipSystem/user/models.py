from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField


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
    nickname = models.CharField(max_length=20, verbose_name='昵称')
    school = models.CharField(max_length=10, default='华东理工大学')
    sex = models.CharField(max_length=2, null=True)
    grade = models.CharField(max_length=5)
    major = models.ForeignKey(Major, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return '<Profile: %s for %s>' % (self.nickname, self.user.username)


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    teacher_name = models.CharField(max_length=10, null=True)
    # teacher_Profile = models.ForeignKey(Profile, on_delete=models.DO_NOTHING, default='00000')

    # grade = models.CharField(max_length=5, null=True)

    # major = models.ForeignKey(Major, on_delete=models.DO_NOTHING)
    skill = models.CharField(max_length=50, null=True)
    enter_time = models.DateTimeField(null=True, blank=True)
    self_introduction = RichTextUploadingField(null=True)

    def __str__(self):
        return self.teacher_name


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
        return self.student_name


def get_nickname(self):
    if Profile.objects.filter(user=self).exists():
        profile = Profile.objects.get(user=self)
        return profile.nickname
    else:
        return ''


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


def get_sex(self):
    if Profile.objects.filter(user=self).exists():
        profile = Profile.objects.get(user=self)
        return profile.sex
    else:
        return ''


def get_major(self):
    if Profile.objects.filter(user=self).exists():
        profile = Profile.objects.get(user=self)
        return profile.major
    else:
        return ''


User.get_nickname = get_nickname
User.get_school = get_school
User.get_sex = get_sex
User.get_major = get_major

User.Profile = get_Profile
