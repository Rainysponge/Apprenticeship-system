from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.urls import reverse
from django.core.paginator import Paginator
from comment.forms import CommentForm, Teacher_CommentForm
from comment.models import Comment, Teacher_Comment
from user.models import Teacher, ReadNum, Student, Major, Profile
from user.utils import read_statistics_once_read, get_seven_days_read_data
from .forms import ApprenticeForm
from .models import Homework, ApprenticeRequest, Relationship


# Create your views here.
# TEST

def teacher_list(request):
    Teacher_list = Teacher.objects.all()
    users = User.objects.all()
    major_list = Major.objects.all()
    # profile = Profile.objects.all()
    # type_users = type(users)
    paginator = Paginator(users, 5)  # 每10页进行分页
    page_num = request.GET.get('page', 1)
    page_of_teachers = paginator.get_page(page_num)

    context = {}
    context['teacher_list'] = Teacher_list
    context['major_list'] = major_list
    context['users'] = users
    # context['type_users'] = type_users
    context['page_of_teachers'] = page_of_teachers
    # context['profile'] = profile

    return render(request, 'Apprenticeship/teacher_list.html', context)


def teacher_major(request, major_pk):
    major = Major.objects.get(pk=major_pk)
    profile_list = Profile.objects.filter(major=major)
    major_list = Major.objects.all()

    # profile = Profile.objects.all()
    # type_users = type(users)
    paginator = Paginator(profile_list, 5)  # 每10页进行分页
    page_num = request.GET.get('page', 1)
    page_of_teachers = paginator.get_page(page_num)

    context = {}
    context['major_list'] = major_list
    context['profile_list'] = profile_list
    # context['major_list'] = major_list
    # context['users'] = users
    # context['type_users'] = type_users
    context['page_of_teachers'] = page_of_teachers
    # context['profile'] = profile

    return render(request, 'Apprenticeship/teacher_major.html', context)


def homework_detail(request):
    homework1 = get_object_or_404(Homework, pk=1)
    # comments = Comment.objects.filter(pk=1)
    comments = Comment.objects.all()

    context = {}
    context['user'] = request.user
    context['comments'] = comments

    data = {'homework_id': homework1.id}  # 用于初始
    context['comment_form'] = CommentForm(initial=data)
    context['homework'] = homework1
    return render(request, 'Apprenticeship/homework_detail.html', context)


def teacher_info_outside(request, user_pk):
    if request.user:
        user = request.user
    else:
        user = ''
    # user_outside = User.objects.filter(pk=user_pk).first()
    # teacher = Teacher.objects.filter(pk=user_pk)    用这个获取为什么是错的？
    user_t = get_object_or_404(User, pk=user_pk)
    teacher = Teacher.objects.get(user=user_t)  # 被评论的对象
    comments = Teacher_Comment.objects.filter(content_object=teacher)

    read_cookie_key = read_statistics_once_read(request, teacher)

    data = {'teacher_id': teacher.id}
    context = {}
    context['comments'] = comments
    context['teacher_comment_form'] = Teacher_CommentForm(initial=data)
    context['user_out'] = user_t
    context['teacher'] = user_t.teacher
    context['user'] = user
    # context['dates'] = dates
    # context['read_num_seven_days'] = read_num_seven_days
    context['key'] = read_cookie_key
    # return render(request, 'Apprenticeship/teacher_info_outside.html', context)
    response = render_to_response('Apprenticeship/teacher_info_outside.html', context)  # 响应
    response.set_cookie(read_cookie_key, 'true')  # 阅读cookie标记
    return response


def student_info_outside(request, user_pk):
    # user_outside = User.objects.filter(pk=user_pk).first()
    # teacher = Teacher.objects.filter(pk=user_pk)    用这个获取为什么是错的？
    user = get_object_or_404(User, pk=user_pk)
    student = Student.objects.get(user=user)  # 被评论的对象
    teacherList = ApprenticeRequest.objects.filter(user=user)
    context = {}
    # context['comments'] = comments
    # context['teacher_comment_form'] = Teacher_CommentForm(initial=data)
    context['teacherList'] = teacherList
    context['user_out'] = user
    context['student'] = user.student
    return render(request, 'Apprenticeship/student_info_outside.html', context)


def homework_list(request):
    context = {}
    return render(request, 'Apprenticeship/homework_list.html', context)


def Apprentice_request(request, teacher_pk):
    teacher = Teacher.objects.get(pk=teacher_pk)
    # if request.user.is_authenticated():
    user = request.user
    if ApprenticeRequest.objects.filter(teacher=teacher, user=user).count() == 0:
        # teacher = Teacher.objects.get(pk=teacher_pk)
        # user = request.user
        apprentice_request = ApprenticeRequest()
        apprentice_request.user = user
        apprentice_request.teacher = teacher
        apprentice_request.result = 0
        apprentice_request.save()
    else:
        Teacher_list = Teacher.objects.all()
        users = User.objects.all()
        major_list = Major.objects.all()
        # profile = Profile.objects.all()
        # type_users = type(users)
        paginator = Paginator(users, 5)  # 每10页进行分页
        page_num = request.GET.get('page', 1)
        page_of_teachers = paginator.get_page(page_num)

        context = {}
        context['teacher_list'] = Teacher_list
        context['major_list'] = major_list
        context['users'] = users
        context['massage'] = '你已经给他发过请求了，请耐心等待！'
        # context['type_users'] = type_users
        context['page_of_teachers'] = page_of_teachers
        # context['profile'] = profile

        return render(request, 'Apprenticeship/teacher_list.html', context)

    referer = request.META.get('HTTP_REFERER', reverse('home'))
    return redirect(referer)


def Apprentice_detail(request):
    user = request.user
    # fliter返回集合不能作为查询，只能用get
    teacher = Teacher.objects.get(user=user)
    apprentice_requests = ApprenticeRequest.objects.filter(teacher=teacher, result=0)
    my_students_requests = ApprenticeRequest.objects.filter(teacher=teacher, result=1)
    response_list = ApprenticeRequest.objects.filter(user=user)
    # waiting_response = ApprenticeRequest.objects.filter(user=user, result=0)
    # isRefused_response = ApprenticeRequest.objects.filter(user=user, result=2)

    # my_students_requests = ApprenticeRequest.objects.filter(teacher=teacher, result=1)

    context = {}
    context['response_list'] = response_list
    # context['waiting_response'] = waiting_response
    # context['isRefused_response'] = isRefused_response
    context['apprentice_requests'] = apprentice_requests
    # 为什么前端可以user.student？？
    context['my_students_requests'] = my_students_requests[0:4]
    context['my_students_nums'] = len(my_students_requests)
    return render(request, 'Apprenticeship/Apprentice_detail.html', context)


# def Apprentice_response(request):
#     user = request.user

#     success_response = ApprenticeRequest.objects.filter(user=user, result=1)
#     waiting_response = ApprenticeRequest.objects.filter(user=user, result=0)
#     isRefused_response = ApprenticeRequest.objects.filter(user=user, result=2)

#     # my_students_requests = ApprenticeRequest.objects.filter(teacher=teacher, result=1)

#     context = {}
#     context['success_response'] = success_response
#     context['waiting_response'] = waiting_response
#     context['isRefused_response'] = isRefused_response

#     return render(request, 'Apprenticeship/ApprenticeResponse.html', context)


def Apprentice_agree(request, requirement_pk):
    # user = request.user
    # student = Student.objects.get(user=user)
    requirement = ApprenticeRequest.objects.get(pk=requirement_pk)
    requirement.result = 1
    requirement.save()

    # relationship = Relationship()
    # relationship.SID = user

    referer = request.META.get('HTTP_REFERER', reverse('home'))
    return redirect(referer)


def Apprentice_refuse(request, requirement_pk):
    # user = request.user
    # student = Student.objects.get(user=user)
    requirement = ApprenticeRequest.objects.get(pk=requirement_pk)
    requirement.result = 2
    requirement.save()

    # relationship = Relationship()
    # relationship.SID = user

    referer = request.META.get('HTTP_REFERER', reverse('home'))
    return redirect(referer)
