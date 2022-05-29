from django.db import models
# importujemy model danych części administracyjnej w której możemy tworzyć użytkowników
# będących administratorami naszej strony.
# Ale tutaj wykorzystamy to tak, że po prostu pobierzemy z modelu danych "użtykownik" wszystkie pola i dodamy swoje pola.
# Tak aby wyszedł model użytkownika który może zrobić swój profil w naszej aplikacji webowej.
# Po prostu pobieramy wpudowane pola z klasy User biblioteki django.contrib.auth.models
# I dodajemy swoje.
from django.contrib.auth.models import User

# Create your models here.

class UserProfileInfo(models.Model):
    # Tworzymy relacje z modelem danych użytkownika z palenu administracyjnego
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Dodamy swoje dodatkowe pola dotyczące użytkownika do pól użytkownika które ma w sobie klasa User z biblioteki django.contrib.auth.models
    portfolio = models.URLField(blank=True)
    picture = models.ImageField(upload_to='fifth_app/profile_pics', blank=True)

    def __str__(self):
        # Wyświetlanie rekordów dancyh o użytkownikach poprzez wbudowane pole które pobraliśmy z
        # django.contrib.auth.models.User
        return self.user.username
