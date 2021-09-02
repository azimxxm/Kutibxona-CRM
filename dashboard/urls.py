from django.urls import path
from . import views

urlpatterns = [
    path('', views.view, name='view'),
    path('forms/', views.forms, name='forms'),
    path('table/', views.table, name='table'),
    path('chart/', views.chart, name='chart'),
]





