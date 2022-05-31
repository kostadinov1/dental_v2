from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordChangeDoneView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from web.accounts.forms import UserRegistrationForm


class UserRegistrationView(CreateView):
    form_class = UserRegistrationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        result = super().form_valid(form)
        # user -> self.object
        # req -> self.request
        login(self.request, self.object)
        return result


class UserLoginView(LoginView):
    template_name = 'accounts/login.html'

    def get_success_url(self):
        return reverse_lazy('home')


@login_required
def logout_view(request):
    logout(request)
    return redirect('home')


class ChangePasswordView(PasswordChangeView, LoginRequiredMixin):
    success_url = reverse_lazy('login')


class ChangePasswordDoneView(PasswordChangeDoneView):
    template_name = 'accounts/login.html'
