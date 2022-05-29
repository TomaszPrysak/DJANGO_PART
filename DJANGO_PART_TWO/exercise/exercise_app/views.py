from django.shortcuts import render
from .models import Users

# Create your views here.

def index(request):
    return render(request, 'exercise_app/index.html')

def users(request):
    users_list = Users.objects.order_by('user_firstname')
    users_dict = {
        'users':users_list
    }
    return render(request, 'exercise_app/users.html', users_dict)
