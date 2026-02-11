from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    salary = models.IntegerField()
    join_date = models.DateField(auto_now_add=True)
    post = models.CharField(max_length=100)

    class Meta:
        db_table = "employee"
        
    def __str__(self):
        return self.name
    

class Course(models.Model):
    name = models.CharField(max_length=100)
    fee = models.IntegerField()
    duration = models.IntegerField()
    
    class Meta:
        db_table = "course"

    def __str__(self):
        return self.name
        
class Event(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    event_name = models.CharField(max_length=100) 

    class Meta:
        db_table = "Event"
        
    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.IntegerField()

    class Meta:
        db_table = "Book"
        
    def __str__(self):
        return self.title
         

