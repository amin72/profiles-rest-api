from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


app_name = 'profiles_api'


router = DefaultRouter()
router.register('profile', views.UserProfileViewSet)


urlpatterns = [
    # login
    path('login/', views.UserLoginAPIView.as_view(), name='login'),

    # profile crud
    path('', include(router.urls)),
]
