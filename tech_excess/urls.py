from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('items/', views.ItemList.as_view(), name='items_list'),
    path('items/<int:pk>', views.ItemDetail.as_view(), name='items_detail'),
    path('items/edit/<int:pk>', views.ItemEdit.as_view(), name='items_edit'),
    path('monitors/', views.MonitorList.as_view(), name='monitors_list'),
    path('keyboards/', views.KeyboardList.as_view(), name='keyboards_list'),
    path('mouses/', views.MouseList.as_view(), name='mouses_list'),
    path('headphones/', views.HeadphoneList.as_view(), name='headphones_list'),
    path('reviews/', views.ItemReviewsList.as_view(), name='reviews_list'),
    path('reviews/create', views.CreateReview.as_view(), name='reviews_create'),
    path('reviews/<int:pk>', views.ItemReviewsDetail.as_view(), name='reviews_detail'),
    path('reviews/<int:pk>/change', views.ItemReviewsChange.as_view(), name='reviews_change'),
    path('user/reviews', views.UsersReviewsList.as_view(), name='user_reviews_list'),
    path('user/wishlists', views.WishlistList.as_view(), name='wishlists_list'),
    path('user/wishlists/<int:pk>', views.WishlistDetail.as_view(), name='wishlists_detail'),
    path('user/carts', views.CartList.as_view(), name='carts_list'),
    path('user/carts/current', views.CartInProgress.as_view(), name='carts_in_progress'),
    path('user/carts/completed', views.CartCompleted.as_view(), name='carts_completed'),
    path('user/carts/<int:pk>', views.CartDetail.as_view(), name='carts_detail'),
]