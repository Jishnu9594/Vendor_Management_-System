from django.db import models
import uuid
from django.core.exceptions import ObjectDoesNotExist
from django.core.serializers import serialize
from django.db import models
from django.contrib.auth.models import AbstractUser
from local_apps.account.managers import CustomUserManager
from django.utils import timezone

# Create your models here.
USER_ROLE = (
    ('Admin', "Admin"),
    ('Staff', "Staff"),
    ("Vendor", "Vendor"),
    ("User", "User"),
    ("Others", "Others"),
)


class User(AbstractUser):
    username = None
    date_joined = None
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    prefix = models.CharField(max_length=10, default="SA")
    first_two_letters = models.CharField(max_length=2, default="AA")
    first_two_numbers = models.IntegerField(default=0)
    last_one_letter = models.CharField(max_length=1, default="A")
    last_two_numbers = models.IntegerField(default=0)
    account_id = models.CharField(max_length=220)
    is_email_verified = models.BooleanField(default=False)
    is_mobile_verified = models.BooleanField(default=False)
    email = models.EmailField(unique=True, blank=False, max_length=200,
                              error_messages={'unique': "A user with that email already exists.", }
                              )
    mobile = models.CharField(max_length=20, unique=True, blank=True, null=True,
                              error_messages={'unique': "A user with that mobile already exists.", }
                              )
    role = models.CharField(choices=USER_ROLE, max_length=100, default='Others',
                            help_text='ID generation depends on the role. Once you submit it will be permanent.'
                            )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    objects = CustomUserManager()

    class Meta:
        ordering = ["-created_at", "-updated_at"]
        verbose_name = 'User'
        verbose_name_plural = "Users"