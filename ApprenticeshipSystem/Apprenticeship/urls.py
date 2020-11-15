from django.urls import path
from . import views

urlpatterns = [
    # http://http://127.0.0.1:8000/Apprenticeship/
    path('teacher/', views.teacher_list, name='teacher_list'),
    path('teacher_outside_info/<int:user_teacher_pk>', views.teacher_info_outside, name='teacher_info_outside'),
    path('homework/1/', views.homework_detail, name='homework_detail'),
    path('homework_list/', views.homework_list, name='homework_list'),
]