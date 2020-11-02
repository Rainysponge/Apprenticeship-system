from django.shortcuts import render, get_object_or_404
from .models import Teacher


# Create your views here.
# TEST

def teacher_list(request):
    # tlist = Teacher.objects.get()

    context = {}
    # context['teacher_list'] = tlist

    return render(request, 'Apprenticeship/teacher_list.html', context)


def teacher_info(request, teacher_pk):
    teacher = get_object_or_404(Teacher, pk=teacher_pk)

    context = {}
    content['teacher'] = teacher
    return render(request, 'Apprenticeship/teacher_info.html', context)
