from django.db import models


# Create your models here.

class Details(models.Model):
    name = models.CharField(max_length=250, null=True)
    duration = models.IntegerField(default=3, null=True, blank=True)
    fees = models.IntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
