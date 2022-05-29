from django.urls import include, path, re_path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'euro2020'

urlpatterns = [
    path('', views.Euro2020HomePage.as_view(), name='euro2020_homepage'),
]
