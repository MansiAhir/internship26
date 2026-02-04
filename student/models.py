from django.db import models

# Create your models here.

class Student(models.Model):
    studentName = models.CharField(max_length=100)
    studentAge = models.IntegerField()
    studentCity = models.CharField(max_length=40)
    studentEmail = models.EmailField(null=True)

    class Meta:
        db_table = "student"

class Product(models.Model):
    productName = models.CharField(max_length=100)
    productPrice = models.IntegerField()
    productDescription = models.TextField()
    productStock = models.PositiveIntegerField()
    productColor = models.CharField(max_length=20,null=True)
    productStatus = models.BooleanField(default=True)
       
    class Meta:
        db_table = "product"

class AddToCart(models.Model):
    cartDetails = models.CharField(max_length=100)
    Quantity = models.IntegerField()
    Price = models.IntegerField()
    Date = models.DateField()

    class Meta:
        db_table = "addtocart"