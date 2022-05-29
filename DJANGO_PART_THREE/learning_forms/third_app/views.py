from django.shortcuts import render
from .forms import FormName

# Create your views here.

def index(request):
    return render(request,'third_app/index.html')

def form_name_view(request):
    form = FormName()
    if request.method == "POST":
        form = FormName(request.POST)
        if form.is_valid():
            print("Weryfikacja datych się powiodła")
            print("Nazwisko: " + form.cleaned_data['name'])
            print("Email: " + form.cleaned_data['email'])
            print("Wiadomość: " + form.cleaned_data['text'])
    dictForm = {
        'form':form
    }
    return render(request, 'third_app/form_page.html', dictForm)
