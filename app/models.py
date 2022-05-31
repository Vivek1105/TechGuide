import email
from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    desc = models.TextField()


# for display the name of user who's fill the contact form 
    def __str__(self):
        return self.name
# by doing this u can also get the email of user 
# def __str__(self):
#         return self.name +" - " + self.email 

