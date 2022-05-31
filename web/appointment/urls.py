from django.urls import path

from web.appointment.views import BookAppointmentView

urlpatterns = (

    path('book-appointment/', BookAppointmentView.as_view(), name='book-appointment'),

)