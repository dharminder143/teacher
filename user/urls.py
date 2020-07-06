from rest_framework.routers import DefaultRouter
from django.urls import path, include

from user import views

router = DefaultRouter()
router.register('users', views.UserViewSet, basename='user-list')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]