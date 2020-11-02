from django.db import models
from Apprenticeship.models import Homework
from django.contrib.auth.models import User


class Comment(models.Model):
    content_object = models.ForeignKey(Homework, on_delete=models.DO_NOTHING)

    text = models.TextField()
    comment_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
