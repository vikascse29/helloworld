from django.db import models

# Create your models here.


class person(models.Model):

    Name = models.CharField(max_length=100)
    Email = models.CharField(max_length = 30)
    City = models.CharField(max_length = 100)

    def __str__(self):
        return self.Name
