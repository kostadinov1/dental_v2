from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from web.accounts.models import Profile
from web.common.helpers import BootstrapFormMixin, DisabledFieldsFormMixin

UserModel = get_user_model()
YEARS_CHOICES = range(1920, 2022)


class CreateProfileForm(forms.ModelForm, BootstrapFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Profile
        exclude = ('user',)
        fields = '__all__'


class EditProfileForm(forms.ModelForm, BootstrapFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Profile
        exclude = ('user',)
        fields = '__all__'


class DeleteProfileForm(forms.ModelForm, BootstrapFormMixin, DisabledFieldsFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        self._init_disabled_fields()

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = UserModel
        fields = ()


class UserRegistrationForm(UserCreationForm, BootstrapFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = UserModel
        fields = ('email',)


class UserChangeAdminForm(UserChangeForm):
    class Meta:
        model = UserModel
        fields =('email',)
