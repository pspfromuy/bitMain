from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="blog-home"),
    path('ourteam/', views.ourteam, name="blog-our-team"),
    path('faqs/', views.faqs, name="blog-faqs"),
    path('search/', views.search, name="blog-search"),
]