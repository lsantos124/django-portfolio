from django.urls import path

from . import views

urlpatterns = [
    path('', views.getblogs, name='getblogs'),
    path('<int:blog_id>/', views.detail, name='detail'),
    path('<str:cat>/', views.getBlogsFromCategory, name='getblogscat'),
]
