from datetime import datetime, date
from django.db import models



# Create your models here.
class ContactsModel(models.Model):
    contact_name = models.CharField(max_length=100)
    contact_phone = models.CharField(max_length=100)
    contact_email = models.EmailField()
    contact_type = models.CharField(max_length=100)
    contact_make = models.CharField(max_length=100)
    contact_message = models.CharField(max_length=300)
    contact_seller = models.CharField(max_length=100)
    contact_date = models.DateField(default=datetime.now)
    def __str__(self):
        return self.contact_name

