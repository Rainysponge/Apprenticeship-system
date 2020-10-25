from django.shortcuts import render


# Create your views here.
# TEST

def teacher_list(request):
    return render(request, 'Apprenticeship/teacher_list.html', {})
