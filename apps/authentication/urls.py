

from django.urls import path
from .views import login_view, register_view
from django.contrib.auth.views import LogoutView

from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
]