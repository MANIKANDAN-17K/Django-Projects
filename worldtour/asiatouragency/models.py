from django.db import models

# Create your models here.
class Tour(models.Model):
    origin_country = models.CharField(max_length=64)
    destination_country = models.CharField(max_length=64)
    number_of_days = models.IntegerField()
    price  = models.DecimalField(max_digits=10, decimal_places=2)
    number_of_people = models.IntegerField(default=1)