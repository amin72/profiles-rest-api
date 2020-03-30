from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


app_name = 'profiles_api'


router = DefaultRouter()
router.register('profile', views.UserProfileViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
