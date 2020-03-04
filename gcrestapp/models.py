from django.db import models
from django.utils.translation import gettext_lazy as _

class Restaurant(models.Model):

    class AvailableStates(models.TextChoices):
        IA = 'IA', _('Iowa')
        MN = 'MN', _('Minnesota')
        WI = 'WI', _('Wisconsin')
        ND = 'ND', _('North Dakota')
        SD = 'SD', _('South Dakota')

    owner = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    website = models.URLField(max_length = 200,default=None, blank=True, null=True,help_text = "Please enter a valid URL.")
    street = models.CharField(max_length=200,default=None, blank=True, null=True)
    city = models.CharField(max_length=100,default=None, blank=True, null=True)
    state = models.CharField(max_length=2,blank=True, null=True,choices=AvailableStates.choices)
    zip = models.CharField(max_length=10,default=None, blank=True, null=True)

    def __str__(self):
        return self.name


class Delivery(models.Model):
    restaurant = models.ForeignKey(Restaurant, related_name='choices', on_delete=models.CASCADE)

    class DeliveryType(models.TextChoices):
        DAILY = 'DY', _('Daily')
        WEEKLY = 'WK', _('Weekly')
        MONTHLY = 'MN', _('Monthly')
        ADHOC = 'AH', _('Ad-Hoc')

    delivery_type = models.CharField(max_length=2,choices=DeliveryType.choices,default=DeliveryType.ADHOC)
    last_delivery = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'to ' + self.restaurant + ' of type' + self.delivery_type

