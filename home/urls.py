from django.contrib import admin
from django.urls import path, include
from . import views
from .views import contact  
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home, name="home"),
    path('formations/dev-web/', views.formations_dev_web, name='formations_dev_web'),
    path('formations/cybersecurite/', views.formations_cybersecurite, name='formations_cybersecurite'),
    path('formations/reseau/', views.formations_reseau, name='formations_reseau'),
    path('formations/dev-mobile/', views.formations_dev_mobile, name='formations_dev_mobile'),
    path('formations/design/', views.formations_design, name='formations_design'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),

    path('contact/', contact, name='contact'),
]
