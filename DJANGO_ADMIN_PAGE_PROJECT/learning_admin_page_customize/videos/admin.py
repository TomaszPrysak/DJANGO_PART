from django.contrib import admin
from . import models

# Register your models here.

# Aby zmienić cokolwiek od strony backendowej w panelu administratora dla konkretnego modelu danych musimy klase nazwać w takiej konwencji:
# nazwa modelu z pliku models.py aplikacji plus "Admin":
# Wówczas zmiana będzie dotyczyła panelu administracyjnego dla tej konkretnej aplikacji.
class MovieAdmin(admin.ModelAdmin):
    fields = ['release_year', 'title', 'length'] # Zmieniliśmy kolejność wyświetlania pól w polu administracyjnym dla konkrentego rekordu danych modelu "Movie" z pliku "models.py" aplikacji "videos".
                                                 # Czyli kolejność wyświetlania pól rekordu danych po tym jak na niego klikniemy i 'wejdziemy' do rekordu.

    search_fields = ['title', 'length'] # Dodaliśmy pole do przeszukiwania danych według pola 'title' lub pola 'length'.
                                        # Należy zaznaczyć, że jest jedno okienko/pole przeszukiwania do którego wpisujemy frazy mogące wystąpić w polu 'title' bądź w polu 'length' w naszym modelu danych.

    list_filter = ['release_year', 'length'] # Dodaliśmy pole z filtrowaniem danych według pól 'title' oraz 'length'.
                                             # Wygląda to tak, że po prawej stronie w naszym modelu danych aplikacji polawi się pole do przefiltrowania danych według pól modelu danych które podaliśmy w liście 'list_filter'.

    list_display = ['title', 'release_year', 'length'] # Zmieniliśmy sposób wyświetlania danych nie w taki sposób jak go wskazaliśmy w pliku models.py poprzez funkcję def __str__(str).
                                                       # Tylko wyświetlimy dane z modelu danych Movie w postaci listy.
                                                       # Każdy rekord danych z modelu w liście będzie zawierać kolumne z danymi z 'title', 'release_year' oraz 'length'.
                                                       # Przyczym jako klikany link bedzie pole jako pierwsze występujące w tej liście.

    list_editable = ['length'] # Edytowanie danych jest możliwe w momencie 'wejścia' do rekordu danych w panelu administracyjnym.
                               # Dodanie listy 'list_editable' pozwoli nam edytować dane prosto z listy wyświetlanych rekordów.
                               # Aby to działało, to musi być również wcześniej zdefiniowana lista 'list_display' która umożliwia wyświetlanie danych w postaci listy.
                               # Natomiast aby można było edytować interesujące nas pola danych to pole to musi się znajdować w obu listach: 'list_display' oraz 'list_editable'.

admin.site.register(models.Movie, MovieAdmin)
admin.site.register(models.Customer)
