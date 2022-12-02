from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.dash,name='dashboard'),
    path('table',views.table1, name='table'),
    path('charts',views.charts, name = 'charts')
    ]