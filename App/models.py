from django.db import models

# Create your models here.
class Events(models.Model):
    event_name=models.CharField(max_length=100)
    participent_name=models.CharField(max_length=100)
    participent_address=models.CharField(max_length=100)

    def __str__(self):
        return self.event_name