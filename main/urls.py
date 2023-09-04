from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('create', views.create, name='create'),
    path('success_created/', views.success_created, name='success'),
    path('error', views.error, name='error'),
    path('<int:pk>', views.Detail_Cloud.as_view(), name='detail')
]
