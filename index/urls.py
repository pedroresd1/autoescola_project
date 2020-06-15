from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index) #get and post req. for insert operations
]