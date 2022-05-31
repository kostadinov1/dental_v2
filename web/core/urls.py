from django.urls import path

from web.core.views import HomeView, AboutView, ContactsView, PricingView, ServicesView, OpenHoursView, BlogHomeView, \
    BlogSingleView, ElementsView

urlpatterns = (
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('pricing/', PricingView.as_view(), name='pricing'),
    path('services/', ServicesView.as_view(), name='services'),
    path('open-hours/', OpenHoursView.as_view(), name='open hours'),
    path('blog-home/', BlogHomeView.as_view(), name='blog home'),
    path('blog-single/', BlogSingleView.as_view(), name='blog single'),
    path('elements/', ElementsView.as_view(), name='elements'),

)