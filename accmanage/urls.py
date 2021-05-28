from django.urls import path
from . import views


app_name = 'accmanage'

urlpatterns = [
    path('', views.index, name='index'),
    path('acc/delete/<int:acc_id>/', views.acc_delete, name='acc_delete'),
]
