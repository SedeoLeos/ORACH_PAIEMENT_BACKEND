# posts/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CotisationViewSet, LoginAPI, UserViewSet ,RegisterAPI, VersementViewSet
from knox import views as knox_views

router = DefaultRouter()
router.register('Users', UserViewSet, 'post')
router.register('cotisation',CotisationViewSet)
router.register('versement',VersementViewSet) 


urlpatterns = [
     path('', include(router.urls)),
     path('register/', RegisterAPI.as_view(), name='register'),
     path('login/', LoginAPI.as_view(), name='login'),
     path('logout/', knox_views.LogoutView.as_view(), name='logout'),
     path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    
]