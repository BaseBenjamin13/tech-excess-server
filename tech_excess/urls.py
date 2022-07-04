from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('monitors/', views.MonitorsList.as_view(), name='monitors_list'),
    path('monitors/<int:pk>', views.MonitorDetail.as_view(), name='monitors_detail'),
    path('keyboards/', views.KeyboardsList.as_view(), name='keyboards_list'),
    path('keyboards/<int:pk>', views.KeyboardDetail.as_view(), name='keyboards_detail'),
    path('mouses/', views.MousesList.as_view(), name='mouses_list'),
    path('mouses/<int:pk>', views.MouseDetail.as_view(), name='mouses_detail'),
    path('headphones/', views.HeadPhonesList.as_view(), name='headphones_list'),
    path('headphones/<int:pk>', views.HeadPhoneDetail.as_view(), name='headphones_detail'),
    path('reviews/', views.ReviewsList.as_view(), name='reviews_list'),
]