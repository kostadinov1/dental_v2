from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'core/index.html'


class AboutView(TemplateView):
    template_name = 'core/about.html'


class ContactsView(TemplateView):
    template_name = 'core/contact.html'


class PricingView(TemplateView):
    template_name = 'core/pricing.html'


class ServicesView(TemplateView):
    template_name = 'core/services.html'


class OpenHoursView(TemplateView):
    template_name = 'core/opening-hour.html'


class BlogHomeView(TemplateView):
    template_name = 'blog/blog-home.html'


class BlogSingleView(TemplateView):
    template_name = 'blog/blog-single.html'


class ElementsView(TemplateView):
    template_name = 'elements.html'

