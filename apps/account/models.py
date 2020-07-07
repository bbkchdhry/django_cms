from django.db import models

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