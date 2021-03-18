from django.db import models

class CalculateHistory(models.Model):
    problem = models.CharField(max_length=100)
    solution = models.CharField(max_length=100)

    def __str__(self):
        return "Problem = " + self.problem, "Solution = " + self.solution
