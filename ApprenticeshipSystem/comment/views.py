#23课28：56
#23课8:20 HTTP_REFERER获取当前页面信息 reverse解析urls中home的路径，这里使用为啥是跳到当前页面？
from django.shortcuts import render, redirect
from .models import Comment
from Apprenticeship.models import Homework
from django.urls import reverse
# Create your views here.


def update_comment(request):
    user = request.user
    #与前端交互
    text = request.POST.get('text', '')
    if text == '':
        #return render(request, 'error.html', {'message：评论内容为空'})
        pass
    try:
        object_id = int(request.POST.get('homework_id', ''))
    except Exceptionas as e:
        # return render(request, 'error.html', {'message：评论对象不存在'})
        pass
    #object_id = int(request.POST.get('homework_id', ''))

    comment = Comment()
    comment.user = user
    comment.text = text
    comment.content_object = Homework.objects.get(pk=object_id)
    comment.save()

    referer = request.META.get('HTTP_REFERER', reverse('home'))
    return redirect(referer)
   # return render(request, 'user/homework.html')

