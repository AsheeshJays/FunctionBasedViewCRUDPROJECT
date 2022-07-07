from django.contrib import admin
from django.urls import path
from mainApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.AddShow,name='addandshow'),
    path('edit/<int:id>/',views.edit,name="edit"),
    path('delete/<int:id>/',views.delete,name="delete")
]
