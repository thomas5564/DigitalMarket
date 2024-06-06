from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    name= models.CharField(max_length=255)
    class Meta:
        _verbose_name_plural="Categories"
        ordering=("name",)
    def __str__(self):
        return self.name
    
class Item(models.Model):
    Category=models.ForeignKey(Category,related_name="items",on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    image=models.ImageField(blank=True,null=True)
    description=models.TextField(blank=True,null=True)
    price=models.FloatField()
    is_sold=models.BooleanField()
    created_by=models.ForeignKey(User,related_name="items",on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering=("Category","name","description","price","is_sold","created_by","created_at")
        verbose_name_plural="Items"
    def __str__(self):
        return self.name