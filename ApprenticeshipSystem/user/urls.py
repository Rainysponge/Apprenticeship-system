from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('changeProfileInfo/<int:profile_pk>', views.changeProfileInfo, name='changeProfileInfo'),

    path('teacher/', views.teacher_info, name='teacher_info'),


]