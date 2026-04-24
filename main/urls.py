from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('ai/', views.ai_page, name='ai'),
]