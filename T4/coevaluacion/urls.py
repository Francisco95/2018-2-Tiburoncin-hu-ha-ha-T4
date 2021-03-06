from django.conf.urls import url

from . import views
from django.urls import path

urlpatterns = [
    path('login/', views.login, name='login'),
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('course/', views.course, name='course'),
    path('coevaluation/', views.coevaluation, name='coevaluation'),
]
