from django.db import models
from django.contrib.auth.models import User
class AddOrder(models.Model):
    TOPPINGS = [
        ("blu","Blueberries"),
        ("ban","Bannana"),
        ("mix","Mixed Berries"),
    ]
    topping = models.CharField(max_length=14, null=False, blank=False, default='Default', choices=TOPPINGS)
    quantity = models.IntegerField("Quantity", null=False, blank=False)
    delivery_date = models.DateField("Date", null=False, blank=False)
    name = models.CharField("Full Name:", null=False, max_length=40)
    email = models.CharField("Email:", max_length=40)
    phone = models.CharField("Phone Number:", null=False, blank=False, max_length=11)
    comments = models.TextField("Additional Comments", max_length=1000)
    delivery_time =models.CharField("Delivery Time:", null=False, blank=False, max_length=10)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}'s Order"
class Promotion(models.Model):
    PROMOTION_CHOICES = [
        ('percentage','Percentage'),
        ('fixed_amount', 'Fixed Amount'),
    ]
    code = models.CharField("Promo-Code", max_length=40, unique=True)
    discount_type = models.CharField(max_length=20, choices=PROMOTION_CHOICES)
    discount_value = models.DecimalField(max_digits=10, decimal_places=2)

class PromotionUsage(models.Model):
    promotion = models.ForeignKey(Promotion, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_used = models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = ('promotion', 'user')
