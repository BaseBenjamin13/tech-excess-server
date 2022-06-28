from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('monitors/', views.MonitorsList.as_view(), name='monitors_list'),
]