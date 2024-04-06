from django.contrib import admin
from django.urls import path,include
import home.views as views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('viewtask/', views.viewtasks, name='viewtasks'),
    path('addtask/', views.addtask, name='addtask'),
]
