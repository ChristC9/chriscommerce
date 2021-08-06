from django.db import models
from category.models import  AllCategories,SubCategories
from django.contrib.auth.models import User
# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField()
    price=models.IntegerField()
    category=models.ForeignKey(AllCategories,on_delete=models.CASCADE)
    subcategory=models.ForeignKey(SubCategories,on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Order(models.Model):
    count=models.IntegerField()
    total=models.IntegerField()
    userId=models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.userId.username
    
    def grandTotal(self):
        gtotal=0
        gtotal+=self.total
        return gtotal
        

class OrderItem(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    image=models.CharField(max_length=100)
    count=models.IntegerField()
    orderId=models.ForeignKey(Order,on_delete=models.CASCADE, related_name="items")
    userId=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def total(self):
        return self.price * self.count
    
    
    # def all_total(self):
    #     alltotal=0
    #     alltotal+=self.total()
    #     return alltotal
    
    
    
        
   