from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.order_list, name='order_list'),
    url(r'create/', views.order_create, name='order_create'),
    path('delete/<int:a_id>/', views.order_delete, name='order_delete'),
    path('update/<int:a_id>/', views.order_update, name='order_update')
]

