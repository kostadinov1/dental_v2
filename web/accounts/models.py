
from django.contrib.auth import models as auth_models
from django.db import models

from web.accounts.managers import AppUsersManager
from web.common.validators import validate_only_letters


class AppUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    email = models.EmailField(unique=True, null=False, blank=False,)
    date_joined = models.DateTimeField(auto_now_add=True,)

    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False,)
    is_active = models.BooleanField(default=True)

    has_profile = models.BooleanField(default=False)

    objects = AppUsersManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Profile(models.Model):
    FIRST_NAME_MIN_LENGTH = 2
    FIRST_NAME_MAX_LENGTH = 30
    LAST_NAME_MIN_LENGTH = 2
    LAST_NAME_MAX_LENGTH = 30

    GENDERS = (('Male', 'Male'), ('Female', 'Female'), ('LGBT+', 'LGBT+'), ('Prefer Not to Tell', 'Prefer Not to Tell'),)

    first_name = models.CharField(max_length=FIRST_NAME_MAX_LENGTH,
                                  validators=(validate_only_letters,))
    last_name = models.CharField(max_length=LAST_NAME_MAX_LENGTH,
                                 validators=(validate_only_letters,))
    dob = models.DateField(null=True, blank=True,)
    gender = models.CharField(max_length=30, choices=GENDERS, null=True, blank=True)
    phone = models.CharField(max_length=10, unique=True)
    image = models.ImageField('image', blank=True, null=True)
    user = models.OneToOneField(AppUser, on_delete=models.CASCADE, primary_key=True,)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

