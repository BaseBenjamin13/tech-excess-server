from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('monitors/', views.MonitorsList.as_view(), name='monitors_list'),
    path('monitors/<int:pk>', views.MonitorDetail.as_view(), name='monitors_detail'),
    path('keyboards/', views.KeyboardsList.as_view(), name='keyboards_list'),
    path('mouses/', views.MousesList.as_view(), name='mouses_list'),
    path('headphones/', views.HeadPhonesList.as_view(), name='headphones_list'),
]