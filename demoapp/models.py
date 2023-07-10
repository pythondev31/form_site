from django.db import models


class Customer(models.Model):
    first_name=models.CharField(max_length=100, blank=False, null=False)
    last_name=models.CharField(max_length=100, blank=False, null=False)
    phone_number=models.CharField(max_length=100, blank=False, null=False)
    email=models.CharField(max_length=100, blank=False, null=False)
    message = models.TextField(blank=False,null=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
# Create your models here.
