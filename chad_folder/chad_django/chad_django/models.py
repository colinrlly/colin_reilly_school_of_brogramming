from django.db import models

class CalculateHistory(models.Model):
    input = models.CharField(max_length=100)
    output = models.CharField(max_length=100)
