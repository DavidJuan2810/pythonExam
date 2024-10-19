from django.db import models
from django.db.models import SET_NULL
# Create your models here.

# Creation of the Product model 
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()

    def __str__(self):
        return self.name
    
# Creation of the Orders model 
class Order(models.Model):
    fkproduct = models.ForeignKey(Product, on_delete=SET_NULL, null = True)
    nombre = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    observaciones = models.TextField(max_length=500)

    def __str__(self):
        return self.nombre