from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('changeProfileInfo/<int:profile_pk>', views.changeProfileInfo, name='changeProfileInfo'),
    path('homework/1/', views.homework_detail, name='homework_detail'),     # 后续改成int[]形式
    path('teacher', views.teacher_list, name='teacher_list'),
    path('teacher/<int:teacher_pk>', views.teacher_info, name='teacher_info'),
    path('homework_list/', views.homework_list, name='homework_list'),
    path('teacher_outside_info/<int:user_pk>', views.teacher_info_outside, name='teacher_info_outside'),
]