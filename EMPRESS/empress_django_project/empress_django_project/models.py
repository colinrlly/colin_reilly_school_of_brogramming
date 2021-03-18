from django.db import models

class CalculateHistory(models.Model):
    input= models.CharField(max_length=100)
    result= models.CharField(max_length=100)
