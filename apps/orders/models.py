from django.db import models
from django.db.models import SET_NULL

# Create your models here.

# Creation of the Product model 
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()

    def __str__(self):
        return self.name

# Creatio of the table model
class Table(models.Model):
    name = models.CharField(max_length=30)
    ability = models.IntegerField()

    def __str__(self):
        return self.name
    
# Creation of the Reservation model 
class Reservation(models.Model):
    table = models.ForeignKey(Table, on_delete=models.SET_NULL, null=True)
    reservation_date= models.DateTimeField()
    number_Of_People = models.IntegerField()

    def __str__(self):
        return self.reservation_date
    
# Creation of the Orders model 
class Order(models.Model):
    fkproduct = models.ForeignKey(Product, on_delete=SET_NULL, null = True)
    fktable = models.ForeignKey(Table, on_delete=SET_NULL, null = True)
    ORDER_STATUS = [('Para Llevar', 'Para Llevar'),('Consumir', 'Consumir')] 
    ORDER_OPTION = [('En Espera', 'En espera'),('Entregado', 'Entregado')]
    nombre = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    observaciones = models.TextField(max_length=500)
    status = models.CharField(max_length=50, choices=ORDER_STATUS, default='Para Llevar')
    option = models.CharField(max_length=50, choices=ORDER_OPTION, default='En espera')

    def __str__(self):
        return self.nombre
    
