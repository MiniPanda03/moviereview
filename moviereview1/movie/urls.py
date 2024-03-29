"""moviereview2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from . import views
from rest_framework import routers
from django.urls import include, path

router = routers.DefaultRouter()
router.register('Director', views.DirectorViewSet)
router.register('Actor', views.ActorViewSet)
router.register('Movie',views.MovieViewSet)
router.register('Rating',views.RatingViewSet)
router.register('User',views.UserViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('add/addrecord/', views.addrecord, name='addrecord'),
    path('api/', include(router.urls)),
    path('api-token-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
