from django.db import models

# Create your models here.

class contact(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.email

class fact(models.Model):
    fact = models.TextField()

    def __str__(self):
        return self.fact