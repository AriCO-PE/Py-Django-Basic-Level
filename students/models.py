from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(blank=True, null=True)
    enrollment_date = models.DateField(auto_now_add=True)
    aura = models.IntegerField(
        blank=True,
        null=True,
        validators=[MinValueValidator(0), MaxValueValidator(10000)]
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
