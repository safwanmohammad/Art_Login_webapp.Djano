from django.urls import path
from . import views
from django.contrib.auth import views as  auth_view

urlpatterns = [
    path('', views.login, name='login'),
    path('logout/', views.logout, name='logout')
]
