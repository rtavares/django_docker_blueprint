from django.db import models

# Create your models here.

class SampleData(models.Model):
    """ Sample data for BluePrint """
    name = models.CharField(max_length=200)
    notes = models.TextField()

    def __str__(self):
        return f"{self.pk} - {self.name}"
