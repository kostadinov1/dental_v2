from django.contrib.auth import login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordChangeDoneView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from web.accounts.forms import UserRegistrationForm, CreateProfileForm, EditProfileForm, DeleteProfileForm
from web.accounts.models import Profile

UserModel = get_user_model()

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


# PROFILE VIEWS
class ProfileDetailsView(DetailView, LoginRequiredMixin):
    model = Profile
    template_name = 'accounts/profile.html'
    context_object_name = 'profile'


class CreateUserProfileView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('home')
    form_class = CreateProfileForm
    template_name = 'accounts/profile-create.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        self.request.user.has_profile = True
        return super().form_valid(form)


class EditProfileView(UpdateView, LoginRequiredMixin):
    model = Profile
    template_name = 'accounts/profile-edit.html'
    form_class = EditProfileForm

    def get_success_url(self):
        return reverse_lazy('show profile view', kwargs={'pk': self.object.user.id})


class DeleteProfileView(DeleteView, LoginRequiredMixin):
    model = UserModel
    template_name = 'accounts/profile-delete.html'
    success_url = reverse_lazy('home')
    form_class = DeleteProfileForm
