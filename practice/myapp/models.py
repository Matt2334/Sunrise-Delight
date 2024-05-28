from django.db import models

# Create your models here.
class AddOrder(models.Model):
    topping = models
    quantity = models.IntegerField()
    delivery_date = models.DateField()
    name = models.CharField("Full Name:", max_length=40)
    email = models.CharField("Email:", max_length=40)
    phone = models.CharField("Phone Number:", max_length=11)
    comments = models.TextField("Additional Comments", max_length=1000)
    delivery_time =models.CharField("Delivery Time:", max_length=10)