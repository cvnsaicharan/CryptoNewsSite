from django.db import models

# Create your models here.
class SignUp(models.Model):
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    username = models.CharField(max_length=50)

    objects = models.Manager()

    def __str__(self):
        return self.username