from django.db import models

# Create your models here.
class fooditem(models.Model):
    image=models.ImageField(upload_to='image/')
    FoodName=models.CharField(max_length=100)
    description=models.TextField()
    price=models.IntegerField()

   