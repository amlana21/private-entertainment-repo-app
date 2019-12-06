from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

# Types like DVD, Games, Comics, movies etc
class ItemTypes(models.Model):
    typename=models.CharField(max_length=64,primary_key=True)

    def __str__(self):
        return self.typename

# Lists like Watchlist, In progress, Owned etc
class ListTypes(models.Model):
    listname=models.CharField(max_length=64,primary_key=True)

    def __str__(self):
        return self.listname

# Sources like Netflix, Netflix DVD etc
class SourceType(models.Model):
    sourcename=models.CharField(max_length=64,primary_key=True)

    def __str__(self):
        return self.sourcename

# actual item rows
class Items(models.Model):
    prrtychoices=(
        ('Hi','High'),
        ('Med','Medium'),
        ('Lo','Low')
    )
    itemname=models.CharField(max_length=255)
    source=models.ManyToManyField(SourceType,related_name='sourcetype')
    listadded=models.ManyToManyField(ListTypes,related_name='lists')
    typeofoitem=models.ForeignKey(ItemTypes,on_delete=models.CASCADE)
    price=models.FloatField(validators=[MinValueValidator(0)])
    resellprice=models.FloatField(validators=[MinValueValidator(0)])
    priority=models.CharField(max_length=64,choices=prrtychoices)


    def __str__(self):
        return self.itemname

    def getpriority(self):
        for v in self.prrtychoices:
            # print(v)
            if v[0]==self.priority:
                return v[1]
    
    def getpriorityval(self):
        outpt=[]
        for v in self.prrtychoices:
            # print('working loop')
            # print(v)
            outpt.append(v[1])
        return outpt

    def getprioritydict(self):
        outpt=[]
        for v in self.prrtychoices:
            tmp={}
            # print('working loop')
            # print(v)
            tmp[v[1]]=v[0]
            outpt.append(tmp)
        return outpt





