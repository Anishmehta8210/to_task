"""
URL configuration for to_task project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from to_list.views import task_list, update_task, delete_task



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', task_list, name='task_list'),
    path('update_task/<int:pk>/', update_task, name='update_task'),
    path('delete_task/<int:pk>/', delete_task, name='delete_task'),
]
