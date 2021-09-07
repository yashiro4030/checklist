from django.db import models
from django.db.models.base import Model

# Create your models here.
class Chekslst(models.Model):
    systeme = models.CharField(max_length=100,null=True)
    service = models.CharField(max_length=100,null=True)
    checked = models.CharField(max_length=100,null=True)
    action =  models.TextField(max_length=500 ,null=True)
    Remarque = models.TextField(max_length=500 ,null=True)

    def __str__(self) -> str:
        return self.systeme
        
