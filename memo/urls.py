from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'memos'
urlpatterns = [
    path('',views.index, name='list'),
    path('create/',views.create, name='create'),
]
