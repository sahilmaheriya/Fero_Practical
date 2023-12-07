from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=122, unique=True)
    weight = models.DecimalField(decimal_places=2, max_digits=8)
    
    def __str__(self) -> str:
        return self.name