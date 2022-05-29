from django.urls import path, re_path
from . import views

urlpatterns = [
    # path('firstway/', views.first_way_url, name='first_way_url'),
    # path('secondway/', views.second_way_url, name='second_way_url')
    re_path(r'^(firstway|secondway)/$', views.one_way_url)
]
