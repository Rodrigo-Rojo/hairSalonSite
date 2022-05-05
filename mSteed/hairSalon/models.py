from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.


class Appointment(models.Model):
    date_created = models.DateTimeField(blank=False)
    client_fname = models.CharField(max_length=200, blank=False, help_text='First Name')
    client_lname = models.CharField(max_length=200, blank=False, help_text='Last Name')
    client_email = models.EmailField(max_length=254, blank=False, help_text='Email')
    client_phone = PhoneNumberField(blank=False, help_text='Contact Phone Number')
    appointment_date = models.DateTimeField(blank=False)
    appointment_notes = models.TextField(help_text='Appointment Notes (Optional)')

    def __str__(self):
        return self.client_fname + self.client_lname
