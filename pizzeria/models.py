from pyexpat import model
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Pizza(models.Model):
    text = models.TextField('pizza_name')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

class Topping(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    text = models.TextField('topping_name')

    class Meta:
        verbose_name_plural = 'toppings'

    def __str__(self):
        return f"{self.text [:50]}..." 