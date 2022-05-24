from django.db import models


class Order(models.Model):
    # buyer = 
    #this will relate to another table that doesn't exist yet
    total_paid = models.IntegerField()
    pub_date = models.DateTimeField('date published')
    suggested = models.IntegerField()
    delta = models.IntegerField()
    # method = models.
    # this will relate to another table
    seller = models.CharField(default="Unknown", max_length=200)
    note = models.CharField(max_length=200)

    def __str__(self):
        return "Order" + self.id

