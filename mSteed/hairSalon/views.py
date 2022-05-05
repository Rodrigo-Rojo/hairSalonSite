from django.shortcuts import render
from .models import Appointment
from django import forms
from phonenumber_field.modelfields import PhoneNumberField
from datetime import datetime, date
from calendar import monthrange


now = datetime.now()
today = now.day
year = now.year
month = now.month
datetime_object = datetime.strptime(str(month), "%m")
full_month_name = datetime_object.strftime("%B")


# Create your views here.
class MyDateInput(forms.DateInput):
    input_type = 'date'


class AppointmentForm(forms.Form):
    first_name = forms.CharField(max_length=200, required=True)
    last_name = forms.CharField(max_length=200)
    email = forms.EmailField(max_length=254)
    phone = forms.CharField(max_length=20)
    notes = forms.CharField(widget=forms.Textarea())
    date = forms.DateField(widget=MyDateInput)


def get_days():
    num_days = monthrange(year, month)[1]
    days = [date(year, month, day) for day in range(1, num_days + 1) if day >= today]
    return days


def index(request):
    # if request.method == 'POST':
    #     form = AppointmentForm(request.POST)
    #     if form.is_valid():
    #         fname = form.cleaned_data['first_name']
    #         lname = form.cleaned_data['last_name']
    #         email = form.cleaned_data['email']
    #         phone = form.cleaned_data['phone']
    #         notes = form.cleaned_data['notes']
    #         date = form.cleaned_data['date']
    #     else:
    hours = [f"{str(i)}:00" for i in range(9, 17)]
    days = get_days()
    form = AppointmentForm()
    return render(request, 'index.html', {'days': days, 'hours': hours, "month": full_month_name})


def make_appointment(request, hour, day):
    form = AppointmentForm(request.POST)

    return render(request, 'appointment.html', {'form': form, 'hour': hour, 'day': day})
