from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator 

class Student(models.Model):
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    email = models.EmailField(unique=True, blank=False)
    date_of_birth = models.DateField(blank=True, null=True)
    enrollment_date = models.DateField(auto_now_add=True)
    aura = models.IntegerField(
        blank=True,
        null=True,
        validators=[MinValueValidator(0), MaxValueValidator(10000)]
    )
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
