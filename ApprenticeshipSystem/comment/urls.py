from django.urls import path
from . import views

urlpatterns = [
    # http://http://127.0.0.1:8000/Apprenticeship/
    path('update_comment/', views.update_comment, name='update_comment'),
]