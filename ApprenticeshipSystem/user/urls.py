from django.urls import path
from . import views

urlpatterns = [
    # http://http://127.0.0.1:8000/Apprenticeship/
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('changeProfileInfo/<int:profile_pk>', views.changeProfileInfo, name='changeProfileInfo'),
    path('homework/1/', views.homework_detail, name='homework_detail'),     #后续改成int[]形式
    path('teacher', views.teacher_list, name='teacher_list'),
    path('teacher/<int:teacher_pk>', views.teacher_info, name='teacher_info'),
]