from django.db import models
# Create your models here.
class Furniture(models.Model):
    heading = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    description = models.TextField()

    def __str__(self):
        return self.heading


