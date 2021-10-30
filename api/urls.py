from django.urls import path, include
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('tasks', views.TaskViewSet)
router.register('news', views.NewsViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('', include('djoser.urls.jwt')),
    path('register/', views.CreateUserView.as_view(), name='register'),
]
