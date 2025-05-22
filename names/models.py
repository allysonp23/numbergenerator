from django.db import models


class GivenName(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    name = models.CharField(max_length=100, unique=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def __str__(self):
        return self.name


class Surname(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
