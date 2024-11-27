from django.db import models

class Drinks(models.Model):
    name=models.CharField(max_length=200)
    description=models.CharField(max_length=500)

    def __str__(self):
        return self.name + "" +self.description

class Users(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    age=models.CharField(max_length=200)

    def __str__(self):
        return self.name