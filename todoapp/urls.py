from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views


urlpatterns = [
    path('',views.taskview,name='taskview'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('covtask/',views.TaskListView.as_view(),name='covtask'),
    path('covdetail/<int:pk>/',views.TaskDetailView.as_view(),name='covdetail'),
    path('covupdate/<int:pk>/',views.TaskUpdateView.as_view(),name='covupdate'),
    path('covdelete/<int:pk>/',views.TaskDeleteView.as_view(),name='covdelete')
]
