from pyexpat import model
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Pizza(models.Model):
    pizza_name = models.CharField(max_length=200)

    def __str__(self):
        return self.text

class Topping(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    topping_name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'toppings'

    def __str__(self):
        return f"{self.text [:50]}..." 


class Comment(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    comment = models.TextField(max_length=200)

    def __str__(self):
        return f"{self.text [:50]}..." 