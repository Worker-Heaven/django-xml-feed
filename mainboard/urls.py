from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('settings/', views.index, name='index'),
    path('settings/sites/new/', views.sites_new, name='sites_new'),
    path('settings/sites/<int:site_id>/', views.sites_details, name='sites_details'),
    path('settings/sites/<int:site_id>/config/new/', views.sites_config_new, name='sites_config_new'),
    path('settings/sites/<int:site_id>/config/<int:config_id>/', views.sites_config_details, name='sites_config_details'),
]
