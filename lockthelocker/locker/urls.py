from django.contrib import admin
from django.urls import path, include

from .views import index, locker, appointment_create, appointment_delete, manage, appointment_initialize, manage_broken

app_name = 'locker'
urlpatterns = [
    path('', index, name='index'),
    path('appointment/', locker, name='appointment'),
    path('appointment/create/<int:locker_id>/', appointment_create, name='appointment_create'),
    path('appointment/delete/<int:user_id>/', appointment_delete, name='appointment_delete'),
    path('manage/', manage, name='manage'),
    path('appointment/initialize/', appointment_initialize, name='appointment_initialize'),
    path('manage/broken/<int:locker_id>', manage_broken, name='manage_broken'),
]