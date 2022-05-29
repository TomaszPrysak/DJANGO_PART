from django.shortcuts import render
from .forms import UserForm, UserProfileInfoForm

from django.contrib.auth import authenticate, login, logout # pomoce biblioteki do tworzenia viewsów logowania i wylogowywania
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required # dektoratory do tworzenia viewsów które obslugują logowanie się użytkownika

# Create your views here.

def index(request):
    return render(request, 'fifth_app/index.html')

@login_required
def special(request):
    return HttpResponse("Zostałeś zalogowany!")

# Bardzo waży views.
# Tutaj wykorzystując wpudowaną bibliotekę logout wylogowujemy z konta użytkownika.
# Jednak abyśmy byli pewni, że wylogowany zostanie tylko ten użytkownik który tego chce to stosujemy dekorator:
# @login_required.
# Super pomocne
@login_required
def user_logut(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()

            registered = True

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    contextDict = {
        'user_form':user_form,
        'profile_form':profile_form,
        'registered':registered,
    }

    return render(request, 'fifth_app/register.html', contextDict)

# Bardzo ważny views. Pokazuje jak budować logikę autoryzacji przy logowaniu.
# Po pierwszepobieramy dane z pól pofmularza za pomocą request.POST.get('nazwaPolaWSzablonieHTML').
# Widać jak dużo Django tutaj nam pomaga poprzez wbudowane metody.
# Jak chociażby metodę authenticate() która w prosty z wykorzystaniem pobierania danych użytkownika z formularza
# na szablonie login.html i potem je sprwadza z tymi w bazie danych.
# Potem jeszcze sprawdzamy sobie czy użytkownik został znaleziony w bazie a potem jeszcze czy jest aktywny.
def user_login(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse("Konto nie jest aktywne")

        else:
            print("Ktoś próbował się zalogować i mu się nie powiodło")
            print("Username: {} and password: {}".format(username, password))
            return HttpResponse("Podano nieprawidłowe dane logowania")

    else:
        return render(request, 'fifth_app/login.html')
