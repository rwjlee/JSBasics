from django.urls import path
from . import views

app_name = 'api_proxy'

urlpatterns = [
    path('', views.index, name='index'),
    path('data', views.data, name='data'),
    path('demo', views.demo, name='demo'),
    path('bill', views.bill, name='bill'),
    path('create_bill', views.create_bill, name='create_bill'),
    path('authenticate_bill/<str:auth_for>', views.authenticate_bill, name='authenticate_bill'),
    path('delete_bill', views.delete_bill, name='delete_bill'),
]