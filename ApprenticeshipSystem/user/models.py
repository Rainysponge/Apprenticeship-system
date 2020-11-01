from django.db import models
from django.contrib.auth.models import User


class Major(models.Model):
    major = models.CharField(max_length=10)

    def __str__(self):
        return 'self.major'


class Sex(models.Model):
    sex = models.CharField(max_length=1)  # 怎么限制男女？？？

    def __str__(self):
        return self.sex


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='昵称')
    nickname = models.CharField(max_length=20)
    school = models.CharField(max_length=10, default='华东理工大学')
    sex = models.CharField(max_length=2, null=True)
    major = models.ForeignKey(Major, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return '<Profile: %s for %s>' % (self.nickname, self.user.username)


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

