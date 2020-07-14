from django.db import models
from apps.roles.models import Role
# Create your models here.
class User(models.Model):
    class Meta:
        db_table = "user"

    user_name = models.CharField(max_length=255, unique=True)
    salt = models.CharField(max_length=255)
    hashed_password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(max_length=255, blank=True)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.user_name


class User_role(models.Model):
    class Meta:
        db_table = "user_roles"

    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    roles = models.ManyToManyField(Role)
