from django.urls import path, re_path
from . import views

# TWORZENIE URL W TEMPLATE TAGGING
# Przy tworzeniu linków relatywnych wykorzystujemy poniższą składnię w pliku html
# <a href="{% url 'left_side:right_side' %}">Link_text</a>

# ZMIENNA Z NAZWA APLIKACJI W TEMPLATE TAGGING
# Tworzymy zienną której wartość będziemy używać po lewej stronie relatywnych linków
# w plikach html w któych będziemy chcieli umieścić link do podstrony naszej pojedynczej aplikacji fourth_app.
app_name = 'fourth_app'

# NAZWY POŁĄCZEŃ VIEWS ZE WZORCAMI ŚCIEŻEK W TEMPLATE TAGGING
# Przy tworzeniu linków relatywnych najpierw musimy stworzyć zmienną z nazwią aplikacji.
# To zostało stworzone powyżej.
# Nastepnie wykorzystujemy nazwane połączone views ze ścieżką w parametrze name.
# I właśnie wartość parametru name umieszczamy po prawej stronie relatywnych linków
# w plikach html w których będziemy chcieli umieścić link do podstrony naszej pojedynczej aplikacji fourth_app.
urlpatterns = [
    path('other/', views.other, name='other'),
    path('relative/', views.relative, name='relative'),
]

# UWAGA !!!
# Powyższe tworzenie linków relatywnych z wykorzystaniem "lewej i prawej strony" odbuwa się tylko wewnątrz
# pojedynczej aplikacji całego projektu. A dokładniej dotyczy linków ustawionych w pliku /fourth_app/urls.py
# Linki relatywne nie wychodzą poza ten plik.
# Jednak jest możliwość do odwołania się do podstron naszego całego projektu.
# Na przykład link do panelu administracyjnego:
# <a href="{% url 'admin:index' %}">THE ADMIN PAGE</a>
# Albo link do strony typu INDEX którą zdefiniowaliśmy w pliku /fourth_project/urls.py:
# <a href="{% url 'index' %}">THE INDEX PAGE</a>
