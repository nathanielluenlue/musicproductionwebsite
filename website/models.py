from django.db import models

# Create your models here.
class Project(models.Model):
    name_text = models.CharField(max_length=200)
    picture = models.ImageField(upload_to=None, height_field=None,
                                width_field=None, max_length=100,)
    
class Band(models.Model):
    name_text = models.CharField(max_length=200)
