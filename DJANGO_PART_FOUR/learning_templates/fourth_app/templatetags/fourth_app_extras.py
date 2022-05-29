from django import template

# Tworzenie własnych filtrów przetwarzających dane przesyłane do szablonów html.
# Filtry pozwalają na prostą obróbkę danych przesłanych do szablonu html właśnie w tym szablonie.
# Nie trzeba ich obrabiać w pliku views.py dla apliakcji tylko robimy to wykorzystując filtry w szablonie.
# Ilość gotowych filtrów jest bardzo duża.
# Aby użyć filtra na jakieś wartości przekazanej do szablonu html musimy po nazwie klucza tej wartości
# postawić pałkę "|" a następnie napisać nazwę filtra którego chcemy użyć.
# Czasami, jeżeli filtr wymaga parametru to po dwukropu w cudzysłowiu wpisujemy wartość argumenty.
# Na przykład:
# <h5>{{ text|upper }}</h5> - na wartości z klucza "text" (jest to jakiś string) stosujemy filtr który oznacza, że wartość tego klucza będzie miła wszystkie litery jako uppercase. Filtr istneijący w Django.
# <h5>{{ number|add:"69" }}</h5> - na wartości klucza "number" (jest to jakiś integer) stosujemy filtr który oznacza, że do wartości z klucza dodajemy liczbę 69. Filtr istniejący w Django.

# Jeżeli chcemy stowyrzć swój filtr to musimy zastosować szablon tworzenia jak poniżej.
# W przykłądnie poniższym filtr polega na usunięciu wartości przekazanej do niego jako parametr.
register = template.Library()

@register.filter(name='cutas') # nazwanie własnego filtr jako "cut". W taki sposób będzie odwoływanie się do filtra w szablonie html.
def cutas(value, arg): # definicja filtra. Do argument "value" przekazujemy wartość klucza którego będziemy poddawać oparacji filtra. Do argumentu "arg" przekazujemy jakiego część wartości klucza z którą coś chcemy zrobić.
    """
    This cuts out all valuse of "arg" from string!
    """
    return value.replace(arg,'cutas') # na całej wartości klucza, pod zmienną "value" używamy metody "replace" która przeszuka całą wartość klucza w poszukiwaniu dopasowania, które przekazaliśmy w zmiennej "arg". I zastąpi wartosć w zmiennej "arg" wartością pusta, czylo "".

# Wywołanie w szablonie html stworzonego przez nas filtra:
# <h5>{{ text|cut:"hello " }}</h5> - wartość klucza "text" (jest to jakiś string) stosujemy stworzony przez nas filtr "cut", który szuka w wartości przypisanej do klucza ciągu znaków "hello" i w definicji filtra zastepuje je pustym ciągiem "". Czyli wycina znalezione dopasowanie i wyrzuca.
