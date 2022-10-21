from distutils.command.upload import upload
from email.policy import default
from pickle import TRUE
from django.db import models

class Hero(models.Model):
    name = models.CharField(max_length=100)
    alias = models.CharField(max_length=50)
    desc = models.CharField(max_length = 200 ,default=TRUE)

    def __str__(self):
        return(self.name)

class Villain(models.Model):
    name = models.CharField(max_length=100)
    alias = models.CharField(max_length=50)
    desc = models.CharField(max_length = 200 , default=TRUE)

    def __str__(self):
        return(self.name)


