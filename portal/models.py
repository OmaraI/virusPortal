#Author: Alfred Ssekagiri (assekagiri@gmail.com)

#Description: This script contains Django models for the East African viral spatial temporal portal.

from django.db import models
from django.utils import timezone
from decimal import Decimal

# Create your models here.    
class virus(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=250)
    scientific_name=models.CharField(max_length=250)
    taxon=models.IntegerField(default=0)

class organism(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=250)
    scientific_name=models.CharField(max_length=250)

class project(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=250)

class site(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=250)
    lat=models.DecimalField(max_digits=10,decimal_places=4,default=Decimal('0.0000'))
    lon=models.DecimalField(max_digits=10,decimal_places=4,default=Decimal('0.0000'))

class sample_type(models.Model):
    id=models.AutoField(primary_key=True)
    type=models.CharField(max_length=250)

class assay(models.Model):
    id=models.AutoField(primary_key=True)
    type=models.CharField(max_length=250)

class instrument(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=250)


class sample(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=250)
    date=models.DateField(default=timezone.now)
    type=models.ForeignKey(sample_type, on_delete=models.CASCADE)
    site=models.ForeignKey(site, on_delete=models.CASCADE)
    organism=models.ForeignKey(organism, on_delete=models.CASCADE)
    assay=models.ForeignKey(assay, on_delete=models.CASCADE)
    instrument=models.ForeignKey(instrument, on_delete=models.CASCADE)
    project=models.ForeignKey(project, on_delete=models.CASCADE)


class sample_virus(models.Model):
    id=models.AutoField(primary_key=True)
    sample=models.ForeignKey(sample,on_delete=models.CASCADE)
    virus=models.ForeignKey(virus,on_delete=models.CASCADE)

