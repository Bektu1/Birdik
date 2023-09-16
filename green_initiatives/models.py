from django.db import models

class GreenInitiative(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    venue = models.CharField(max_length=255)
    picture = models.ImageField(upload_to='initiative_pics/')
    time_and_date = models.DateTimeField()

    def __str__(self):
        return self.name
