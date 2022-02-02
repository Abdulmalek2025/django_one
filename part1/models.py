from django.db import models

# Create your models here.
class Flower(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField()
    description = models.TextField(max_length=4000)

    def __str__(self):
        return self.title