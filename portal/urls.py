from django.urls import path, include
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('summary/', views.summary, name='summary'),
    path('guidelines/', views.guidelines, name='guidelines'),
    path('contact/', views.contact, name='contact'),
    path('publications/', views.publications, name='publications'),
]
