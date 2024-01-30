from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'blog-name'),
    path('about/', views.about, name = 'about-name'), 
    path('contact/', views.contact, name = 'contact-name'),
]