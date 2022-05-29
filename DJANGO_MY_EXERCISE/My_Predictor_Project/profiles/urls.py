from django.urls import include, path, re_path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'profiles'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='profiles/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('succeslogin/', views.SuccesLoginPage.as_view(), name='succes_login'),
    path('succeslogout/', views.SuccesLogoutPage.as_view(), name='succes_logout'),
    path('successignup/', views.SuccesSignupPage.as_view(), name='succes_signup'),
]
