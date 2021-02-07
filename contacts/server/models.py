from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=16, blank=True, default='')
    def __str__(self):
        return self.name