from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView

from web.appointment.forms import AppointmentForm
from web.appointment.models import Appointment


class BookAppointmentView(CreateView):
    template_name = 'appointment/book-appointment.html'
    queryset = Appointment.objects.all()
    form_class = AppointmentForm
