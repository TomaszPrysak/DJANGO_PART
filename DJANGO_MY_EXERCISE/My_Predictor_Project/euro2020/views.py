from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, TemplateView

from . import models

# Create your views here.

class Euro2020HomePage(TemplateView):
    template_name = 'euro2020/euro2020_base.html'
