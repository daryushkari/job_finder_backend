from django.db import models


# Create your models here.


class Applicant(models.Model):
    user_name = models.CharField(max_length=50)
    password_hash = models.CharField(max_length=250)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    resume_address = models.CharField(max_length=100)


class Corporate(models.Model):
    user_name = models.CharField(max_length=50)
    password_hash = models.CharField(max_length=250)
