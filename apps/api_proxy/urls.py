from django.urls import path
from . import views

app_name = 'api_proxy'

urlpatterns = [
    path('', views.index, name='index'),
    path('data', views.data, name='data'),
]