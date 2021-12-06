from django.db import models
from django.db.models.deletion import CASCADE


class Gallery(models.Model):
    image = models.ImageField(upload_to="gallery/")
    category = models.ForeignKey("web.Category",on_delete=models.CASCADE,null=True,blank=True)

 


class Category(models.Model):
    name = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(null=True,blank=True)
    message = models.TextField()

    def __str__(self):
        return self.name


class Address(models.Model):
    details = models.TextField(null=True,blank=True)


class Details(models.Model):
    image = models.FileField(upload_to="details/")
    title = models.CharField(max_length=255,null=True,blank=True)
    description = models.TextField()

    def __str__(self):
        return  self.title



    