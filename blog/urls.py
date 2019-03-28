from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="blog-index"),
    path('home/', views.home, name="blog-home"),
    path('ourteam/', views.ourteam, name="blog-our-team"),
    path('faqs/', views.faqs, name="blog-faqs"),
    path('search/', views.search, name="blog-search"),
    path('mylist/', views.mylist, name="blog-mylist"),
    path('addVideo/', views.addvideo, name="blog-add-video"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)