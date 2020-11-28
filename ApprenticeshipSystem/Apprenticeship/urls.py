from django.urls import path
from . import views

urlpatterns = [
    # http://http://127.0.0.1:8000/Apprenticeship/
    path('teacher/', views.teacher_list, name='teacher_list'),
    path('teacher_outside_info/<int:user_pk>', views.teacher_info_outside, name='teacher_info_outside'),
    path('homework/1/', views.homework_detail, name='homework_detail'),
    path('homework_list/', views.homework_list, name='homework_list'),
    path('Apprentice_request/<int:teacher_pk>', views.Apprentice_request, name='Apprentice_request'),
    path('require/', views.Apprentice_detail, name='Apprentice_detail'),
    path('Apprentice_agree/<int:requirement_pk>', views.Apprentice_agree, name='Apprentice_agree'),
    path('Apprentice_refuse/<int:requirement_pk>', views.Apprentice_refuse, name='Apprentice_refuse'),
]