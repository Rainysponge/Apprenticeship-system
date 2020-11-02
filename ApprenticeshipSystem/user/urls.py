from django.urls import path
from . import views

urlpatterns = [
    # http://http://127.0.0.1:8000/Apprenticeship/
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('homework/', views.homework, name='homework'),
]