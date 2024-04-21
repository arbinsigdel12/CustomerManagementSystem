from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=200,null=True)
    phone = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200,null=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
     return self.name

class Tag(models.Model):
   name=models.CharField(max_length=200,null=True)
   def __str__(self):
     return self.name
    
class Work(models.Model):
   CATEGORY=(
           ('Urgent','Urgent'),
           ('Default','Default'),
           )
   title=models.CharField(max_length=200,null=True)
   description=models.TextField(max_length=200,null=True,blank=True)
   category=models.CharField(max_length=200,null=True,choices=CATEGORY)
   date_assigned=models.DateTimeField(auto_now_add=True,null=True)
   tags=models.ManyToManyField(Tag)
   def __str__(self):
     return self.title

class Order(models.Model):
    STATUS=(
           ('Completed','Completed'),
           ('Incompleted','Incompleted'),
           )
    
    employee=models.ForeignKey(Employee,null=True,on_delete=models.SET_NULL)
    work=models.ForeignKey(Work,null=True,on_delete=models.SET_NULL)
    status=models.CharField(max_length=200,null=True,choices=STATUS)
    date_assigned=models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
     return self.work.title