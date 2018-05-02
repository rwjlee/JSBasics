from django.urls import path
from . import views

app_name = 'login_reg'

urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('authenticate_ajax/<str:auth_for>', views.authenticate_ajax, name='authenticate_ajax'),
]