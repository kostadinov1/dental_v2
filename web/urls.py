from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('web.accounts.urls')),
    path('', include('web.core.urls')),
    path('appointment/', include('web.appointment.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
