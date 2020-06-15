from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.cliente_form, name="cliente_insert"), #get and post req. for insert operations
    path('<int:id>/', views.cliente_form, name="cliente_update"), #get and post req. for update operations
    path('delete/<int:id>/', views.cliente_delete, name="cliente_delete"),
    path('list/', views.cliente_list, name="cliente_list"), # get req. to retrieve and display all records
]
