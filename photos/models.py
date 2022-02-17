from distutils.command.upload import upload
from sre_constants import CATEGORY
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
CAEGORY_CHOICES = {
    ('My Life','ALL'),
    ('Love','Love'),
    ('Adventures','Adventure'),
}

class Category(models.Model):
    name = models.CharField(choices=CAEGORY_CHOICES, max_length=50)

    def __str__(self):

        return str(self.id)
    
class Photo(models.Model):
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    image = models.ImageField(null=True,upload_to='images')
    desc = models.CharField(max_length=100)


