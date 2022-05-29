from django.urls import path, re_path
from . import views

app_name = "blog"

urlpatterns = [
    path('', views.all_post_list, name='all_post_list'),
    path('<slug:slug>', views.post_detail, name='post_detail'),
    path('<slug:slug>/remove/', views.post_remove, name='post_remove'),
    path('postremovesucces/', views.post_remove_succes, name='post_remove_succes'),
    path('category/<slug:slug_category>', views.category_post_list, name='category_post_list'),
    path('category/<slug:slug_category>/remove/', views.category_remove, name='category_remove'),
    path('subcategory/<slug:slug_subcategory>', views.subcategory_post_list, name='subcategory_post_list'),
    path('subcategory/<slug:slug_subcategory>/remove/', views.subcategory_remove, name='subcategory_remove'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logut, name='user_logut'),
    path('newpost/', views.new_post_form, name='new_post_form'),
    path('succeslogin/', views.succes_login, name='succes_login'),
    path('succeslogout/', views.succes_logout, name='succes_logout'),
    path('failedlogin/', views.failed_login, name='failed_login'),
    path('newcategory/', views.new_category_form, name='new_category_form'),
    path('newsubcategory/', views.new_subcategory_form, name='new_subcategory_form'),
]
