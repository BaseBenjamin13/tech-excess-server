from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('items/', views.ItemList.as_view(), name='items_list'),
    path('items/<int:pk>', views.ItemDetail.as_view(), name='items_detail'),
    path('monitors/', views.MonitorList.as_view(), name='monitors_list'),
    path('keyboards/', views.KeyboardList.as_view(), name='keyboards_list'),
    path('reviews/', views.ItemReviewsList.as_view(), name='reviews_list'),
    path('reviews/<int:pk>', views.ItemReviewsDetail.as_view(), name='reviews_detail'),
]


    # path('keyboards/', views.KeyboardsList.as_view(), name='keyboards_list'),
    # path('keyboards/<int:pk>', views.KeyboardDetail.as_view(), name='keyboards_detail'),
    # path('mouses/', views.MousesList.as_view(), name='mouses_list'),
    # path('mouses/<int:pk>', views.MouseDetail.as_view(), name='mouses_detail'),
    # path('headphones/', views.HeadPhonesList.as_view(), name='headphones_list'),
    # path('headphones/<int:pk>', views.HeadPhoneDetail.as_view(), name='headphones_detail'),