from django.urls import path
from .import views


urlpatterns =[
    path('', views.index, name='index'),
    path('contact/', views.contact, name='users-contact'),
    path('about/', views.about, name='users-about'),
    path('home/', views.home, name='users-home'),
]