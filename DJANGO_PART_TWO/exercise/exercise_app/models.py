from django.db import models

# Create your models here.

class Users(models.Model):
    user_firstname = models.CharField(max_length=254)
    user_lastname = models.CharField(max_length=254)
    user_email = models.EmailField(max_length=254, unique=True)

    def __str__(self):
        return self.user_firstname + ' ' + self.user_lastname
