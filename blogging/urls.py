from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_home, name='blog_home'),
    path('post/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('search/', views.search_view, name='blog-search'),
]
