import datetime

from django import forms

from web.appointment.models import Appointment
from web.common.helpers import BootstrapFormMixin

YEARS_CHOICES = range(datetime.date.today().year, datetime.date.today().year + 1)


class AppointmentForm(forms.ModelForm, BootstrapFormMixin):
    def __init__(self,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Appointment
        exclude = ('user', )