from django.db import models
from django.urls import reverse

# Create your models here.

class School(models.Model):
    name = models.CharField(max_length=256)
    principal = models.CharField(max_length=256)
    location = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    # metoda do osbługi szablonu widoku odpowiedzialnego za dodawanie nowych danych do tablei danych według modelu danych w którym ta metoda się znajduje
    # po ddoaniu nowych danych zostanie wywołany odpowiedni wydok
    def get_absolute_url(self):
        return reverse("sixth_app:detail", kwargs={'pk':self.pk})

class Student(models.Model):
    name = models.CharField(max_length=256)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School, related_name='students', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
