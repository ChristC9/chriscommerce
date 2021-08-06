from django.db import models
# from django.db.models.fields import CharField

# Create your models here.
class AllCategories(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField()
    def __str__(self):
        return self.name

class SubCategories(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField()
    parent=models.ForeignKey(AllCategories,on_delete=models.CASCADE)
    def __str__(self):
        return self.name