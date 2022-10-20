from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    imgpath = models.TextField()


class Branch(models.Model):
    latitude = models.CharField(max_length=50)
    longitude = models.CharField(max_length=50)
    address = models.CharField(max_length=50)


class Contact(models.Model):
    types = [
        (1, 'phone'),
        (2, 'facebook'),
        (3, 'email')
    ]
    type = models.IntegerField(choices=types)
    value = models.CharField(max_length=50)


class Course(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    logo = models.CharField(max_length=50)
    contacts = models.ManyToManyField(Contact)
    branches = models.ManyToManyField(Branch)

