from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=10)
    zipcode = models.CharField(max_length=6)


class SelfAssessment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    symptoms_choices = [
        ('fever', 'fever'),
        ('cold', 'cold'),
        ('cough', 'cough')
    ]
    symptoms = models.CharField(choices=symptoms_choices, max_length=5)
    travelHistory = models.BooleanField()
    contactWithCovidPatient = models.BooleanField()



