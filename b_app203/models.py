from django.db import models

# Create your models here.

#0203 demo for menu
class Menu(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField(null=False)
    menu_item_description = models.TextField(max_length=1000, default='')

    def __str__(self):
        return self.name


#0203 demo for booking
class Booking(models.Model):
    first_name = models.CharField(max_length=200)
    reservation_date = models.DateField()
    reservation_slot = models.SmallIntegerField(default=10)

    def __str__(self):
        return self.first_name
