from django.urls import path, re_path
from . import views

# Post urls.py

app_name = 'post'

urlpatterns = [
    path('', views.ListPost.as_view(), name='all'),
    path('new/', views.CreatePost.as_view(), name='create'),
    path('by/<username>/', views.UserPost.as_view(), name='for_user'),
    path('by/<username>/<pk>/', views.DetailPost.as_view(), name='single'),
    path('delete/<pk>/', views.DeletePost.as_view(), name='delete'),
]
