from django.shortcuts import render
from .forms import NewUserForm

# Create your views here.

def index(request):
    return render(request, 'exercise_app/index.html')

def users(request):
    form = NewUserForm()
    dictForm = {
        'form':form
    }
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("Błąd podczas walidacji danych z formularza")
    return render(request, 'exercise_app/users.html', dictForm)
