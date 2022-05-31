from django.contrib.auth import get_user_model
from django.db import models

from web.core.models import Service

UserModel = get_user_model()


class Appointment(models.Model):
    VENUES = (('Balchik', 'Balchik'), ('Kavarna', 'Kavarna'), ('Varna', 'Varna'),)

    venue = models.CharField(max_length=20, choices=VENUES)
    time = models.TimeField()
    date = models.DateField()
    date_added = models.DateTimeField(auto_now_add=True)
    message = models.TextField()
    # has_booking = models.BooleanField(default=False)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'Appointment at {self.venue} on {self.date} at {self.time}'
