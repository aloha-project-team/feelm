from django.db import models

# Create your models here.

class Report(models.Model):
    emotion = models.CharField(max_length=30)
    report = models.TextField()
    recommendation = models.TextField()

    def __str__(self):
        return f'{self.id} : {self.emotion}'