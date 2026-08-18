from django.db import models

class About(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=700, blank=False)
    image = models.ImageField(upload_to='about/', blank=False)

    def __str__(self):
      return self.title
    
class Slider(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=700, blank=False)
    image = models.ImageField(upload_to='slider/', blank=False)    

    def __str__(self):
      return self.title

class Client(models.Model):
    name = models.CharField(max_length=100, blank=False)
    link = models.CharField(max_length=400, blank=False)
    image = models.ImageField(upload_to='client/', blank=False)    

    def __str__(self):
      return self.name    

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    def __str__(self):
      return self.name        