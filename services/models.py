from django.db import models

# Create your models here.

class services(models.Model):
    service_name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    create_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.service_name
