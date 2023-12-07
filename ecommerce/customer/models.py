from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=122, unique=True)
    contact_number = models.CharField(max_length=16)
    email = models.EmailField(max_length=122)
    
    def __str__(self) -> str:
        return self.name