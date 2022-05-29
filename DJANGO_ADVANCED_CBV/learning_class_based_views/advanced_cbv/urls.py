"""advanced_cbv URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from sixth_app import views

urlpatterns = [
    # path('', views.index, name="index"), - tak przypisujemy widoki do wzorców ścieżek http jeżeli wykorzystujemy tworzenie widoków jako funkcji
    # path('', views.CBViewSimplyIndex.as_view()), - tak przypisujemy widok stworzony w konwencji class-based-views w sposób odręczny do wzorców ścieżek http
    path('', views.IndexView.as_view(), name="index"), # tak przypisujemy widok stworzony w konwencji class-based-views z wykorzystaniem szablonów do wzorców ścieżek http
    path('sixth_app/', include('sixth_app.urls', namespace='sixth_app')),
    path('admin/', admin.site.urls),
]
