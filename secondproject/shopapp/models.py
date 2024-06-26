from django.db import models
from django.utils.timezone import now


class Client(models.Model):
    name = models.CharField(max_length=20, blank=False)
    email = models.EmailField(blank=False)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    date = models.DateField(default=now().date())

    def __str__(self):
        return f"Name: {self.name}, email: {self.email}, phone: {self.phone}, address: {self.address}, date: {self.date}"


class Product(models.Model):
    name = models.CharField(max_length=50, blank=False)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    quantity = models.IntegerField()
    date = models.DateField(default=now().date())


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, blank=False)
    product = models.ManyToManyField(Product, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    date = models.DateField(default=now().date())
