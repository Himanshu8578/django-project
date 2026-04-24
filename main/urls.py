from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('virtual-bg/', views.virtual_bg, name='virtual_bg'),
]
path('', views.home, name='home'),
from .views import ai_response

urlpatterns = [
    path('ai/', ai_response, name='ai'),
]
from .views import ai_page

urlpatterns = [
    path('ai/', ai_page, name='ai'),
]