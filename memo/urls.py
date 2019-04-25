from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'memos'
urlpatterns = [
    path('',views.index, name='list'),
    path('create/',views.create, name='create'),
    path('<int:memo_id>/update/',views.update,name='update'),
    path('<int:memo_id>/delete/',views.delete,name='delete'),
    path('<int:memo_id>/like/',views.like,name='like'),
]
