from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.
class CustomUser(AbstractUser):

    class UserType(models.TextChoices):
        CUSTOMER = "CUSTOMER", "Customer"
        SUPPLIER = "SUPPLIER", "Supplier"
        ADMIN = "ADMIN", "Admin"

    # base_role = Role.ADMIN

    username = models.CharField(max_length=50, unique=True, blank=False)
    email = models.EmailField(unique=True, blank=False)
    phone_number = models.CharField(max_length=15, unique=True)
    user_type = models.CharField(_("UserType"), max_length=50, choices=UserType.choices, default=UserType.CUSTOMER)

    def __str__(self):
        return self.username
    
