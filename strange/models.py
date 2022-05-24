from django.db import models
from django.contrib.auth.models import User

class Payment(models.Model):
    method = models.CharField(max_length=200)
    multiplier = models.IntegerField(default=1)

    def __str__(self):
        return self.method
        
class Order(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    total_paid = models.IntegerField()
    pub_date = models.DateTimeField('date published')
    suggested = models.IntegerField()
    delta = models.IntegerField()
    method = models.ForeignKey(Payment, on_delete=models.CASCADE, default=1)
    seller = models.CharField(default="Unknown", max_length=200)
    note = models.CharField(max_length=200)


    def __str__(self):
        return "Order" + self.seller

class Item(models.Model):
    order_number = models.ForeignKey(Order, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    set_name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
