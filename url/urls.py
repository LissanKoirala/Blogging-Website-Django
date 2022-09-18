from django.urls import path
from . import views

urlpatterns = [
    path('<slug:slug>/', views.redirector_view),
    path('', views.home_view),
    path('api/shorten-url/', views.url_shortener_api, name='url_shortener_api'),
    path('api/shorten-url', views.url_shortener_api, name='url_shortener_api_safe'),
]