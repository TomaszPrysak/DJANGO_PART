from django.shortcuts import render

# Importujemy poniższą bibliotekę w momencie jeżeli chcemy tworzyć viewsy za pomocą konwecji class-based-views
from django.views.generic import View # jeżeli tworzymy viewsa w sposób odręczny
from django.views.generic import TemplateView # jeżeli tworzymy viewsa wykorzystując szablony zwany TemplateView
from django.views.generic import ListView # jeżeli tworzymy viewsa wykorzystując szablony zwany ListView
from django.views.generic import DetailView # jeżeli tworzymy viewsa wykorzystując szablony zwany DetailView
from django.views.generic import CreateView, UpdateView, DeleteView # viewsy potrzebne do zrealizowania konwencji CRUD
                                                                    # CreateView pozwoli nam stworzyć/doddać nowe dane do bazy danych aplikacji
                                                                    # UpdateView pozwoli zakutalizaować już istniejące dane w bazie danych aplikacji
                                                                    # DeleteView pozwoli usunąć istniejące dane z bazy danych aplikacji
from django.urls import reverse_lazy
# from django.http import HttpResponse

from . import models

# Create your views here.

# Przykłd poniższy stworzenia widoku za pomocą funkcji.
# def index(request):
#     return render(request, 'sixth_app/index.html')

# Powyższy views teraz stworzymy w konwecji class-based-views.
# Ten views stworzymy w sposób "odręczny". To znaczy, że musimy zaimportować HttpResponse, stworzyć metodę w klasie.
# Taka konwencja jest dużo bardziej wszechstronna.
# Pozwala na proste dziedziczenie jej i ma jeszcze wiele innych zalet o których nie wiem jeszcze :P
# class CBViewSimplyIndex(View):
#     def get(self, request):
#         return HttpResponse('Tworzenie w konwecji CLASS-BASED-VIEWS jest gites!')

# Teraz stworzymy views w konwencji class-based-views ale z wykorzystaniem TemplateView.
# Wykorzystaniech szablonów widoków pozwala uprościć kod.
# Nie musimy importować HttpResponse.
# Inaczej mówiąc nie musimy tworzyć viewsa w sposób odręczny.
class IndexView(TemplateView):
    template_name = 'sixth_app/index.html'
    # jeżeli chcemy do szablonu html przekazać jakieś dane to korzystany z poniższej konstrukcji
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # tego nie musisz rozgryzać choć możesz
        # context['wstrzyknij_mnie'] = "Kurde bele balans" - można tak budować słownik. Ja jednak wolę poniższy sposób
        context = {
            'wstrzyknij_mnie':"Kurde bele balans"
        } # tutaj już jest budowanie słownika z danymi. Słownik ten jest przekazywany do szablonu html
        return context

# Tworząc widoki za pomocą konwencji class-based-views możemy skorzystać z gotowych szablonów widoków.
# I to jest ich największa zaleta, że mamy gotowce w zależności od tego co chcemy wyświetlić i jak chcemy to zrobić.
# Dwa najpopularniejsze szablony widoków to ListView i DetailView.
# I te dwa szablony przydadzą się nam w większości przypadków.
# Za pomocą ListView dane z przypisanego do niego modelu danych są przekazywane do szablonu html w postaci listy.
# Czyli w szablonie html można iterować po liście danych stworzonych automatycznie przez szablon widoku ListView.
# Z kolei szablon DetailView dane z przypisanego do niego modelu danych przekazuje do szablonu html w ten sposob, że może możemy wyświetlać składowe tego modelu danych.
# Podsumowując szablony widoków w konwencji class-based-view pozwalają na szybszą i dedykowaną obsługę i wyświetlanie danych.
# Każdy szablon widoku w inny sposób przedstawia dane z przypisanego do niego modelu danych.
# I ten inny sposób jest przewagą konwencji CBV ponieważ, możemy dobrać taki szablon widoku za pomocą którego szybko i precyzyjnie przedstawimy dane w szablonie html.
# Nie będziemy musieli je pobierać z modelu, obrabiać i dopiero wysylać do szablonu html.

class SchoolListView(ListView):
    template_name = 'sixth_app/school_list.html' # nie musimy określać szablonu html w przypadku tego rodzaju szablonu widoku.
                                                 # Django sam się domysli jaki szablon html będzie pasować do danego widoku po używanych w tym szabloni html.
                                                 # Wynika to z nazwa i rodzajów zmienncyh odpowiadającym danym z danego widoku.
    context_object_name = 'schools'
    model = models.School

class SchoolDetailView(DetailView):
    template_name = 'sixth_app/school_detail.html' # nie musimy określać szablonu html w przypadku tego rodzaju szablonu widoku.
                                                   # Django sam się domysli jaki szablon html będzie pasować do danego widoku po używanych w tym szabloni html.
                                                   # Wynika to z nazwa i rodzajów zmienncyh odpowiadającym danym z danego widoku.
    context_object_name = 'school_detail'
    model = models.School

# Szablony widoków pozwalają nam również na tworzenie widoków które będą mieć formularz pozwalający na dodawanie nowych danych do naszej bazy danych.
# Poza dodawaniem, możemy również stworzyć widoki z formularzami do aktualizowania danych oraz do usuwania danych.
# Takie szablony upraszczają pracę z formularzami wykorzystywanymi do obsługi danych dla użytkowników zewnętrznych. Nie będących administratorami.
# W bradzo prosty sposób tworzymy formularze odpowiadające modelowi danych wystepujących w naszej bazie danych.
# Nie musimy tworzyć pomocniczego pliku forms.py z naszymi modelami formularzy.
# Wykorzystując szablony widoków prosto tworzymy formularze które pozwalają dodawać, edytować usuwać dane z bazdy danych.
# Każdy szablon widoku odpowiedzialny za konkretną interakcję z danymi musi mieć przypisany odpowiedni modela danych z pliku models.py.
# Następnie w modelu danych musimy umieścić odpowiednią metodą do obsługi tych formualrzy z szablonów widoków.
# Tak jak w przypadku poprzednich szablonów widoków tak tutaj przy szablonach CreateView, UpdateView oraz DeleteView nie musimy im przypisywać szablonów html.
# Django samo się domyśli po stosowanych zmiennych w szablonach html który z nich ma zastosować.
# Jest to troche nieintuicyjne. Dla mnie zawsze lepiej coś zdefiniować. Czyli lepiej byłoby przypisać dla widoków konkretny szablon html.
# W konwencji CBV django samo się domyśli, że szablon który stworzyliśmy ma przypisać do stworzonego przez nas widoku w konwencji CBV.

class SchoolCreateView(CreateView):
    fields = ('name', 'principal', 'location')
    model = models.School

class SchoolUpdateView(UpdateView):
    fields = ('name', 'principal')
    model = models.School

class SchoolDeleteView(DeleteView):
    # template_name = 'sixth_app/school_confirm_delete.html'
    model = models.School
    success_url = reverse_lazy("sixth_app:list") # w momencie jak z powodzeniem usunięta zostanie jedna ze szkół to wróć do widoku przedstawiającego listę szkół
