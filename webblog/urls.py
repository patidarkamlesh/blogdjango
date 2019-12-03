from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('blog/<int:pk>/', views.blog_page, name="blog")
]