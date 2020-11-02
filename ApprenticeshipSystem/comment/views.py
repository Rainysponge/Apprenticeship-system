#23课28：56
from django.shortcuts import render
from .models import Comment
from Apprenticeship.models import Homework
# Create your views here.


def update_comment(request):
    user = request.user
    text = request.POST.get('text', '')
    object_id = int(request.POST.get('homework_id', ''))

    comment = Comment()
    comment.user = user
    comment.text = text
    comment.content_object = Homework.objects.get(pk=object_id)
    comment.save()

    return render(request, 'user/homework.html')

