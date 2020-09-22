from django.db import models

# Create your models here.

class Report(models.Model):
    emotion = models.CharField(max_length=30)
    report = models.TextField()
    recommendation = models.TextField()
    recommendation2 = models.TextField(null=True)
    recommendation3 = models.TextField(null=True)

    def __str__(self):
        return f'{self.id} : {self.emotion}'