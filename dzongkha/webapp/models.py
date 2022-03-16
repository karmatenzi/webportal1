from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.
class DzongkhaWord(models.Model):
    phelkay= models.CharField(max_length=70)
    zhebsa= models.CharField(max_length=70)
    phrases= models.CharField(max_length=150)
    audio=models.FileField(upload_to='document/')

    def __str__(self):
       return self.phelkay

class ContactDetails(models.Model):
    firstname=models.CharField(max_length=70)
    lastname=models.CharField(max_length=70)
    email= models.EmailField(max_length=70)
    comments= models.TextField()

    def __str__(self):
       return self.firstname