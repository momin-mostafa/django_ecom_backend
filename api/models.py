from django.db import models

# Create your models here.
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=500,)
    picture = models.ImageField(null=True)
    price = models.CharField(max_length=20,default=0)
    discount = models.FloatField(default=0)
    inStock = models.BooleanField(default=False)
    # completed = models.BooleanField(default=False,blank=True,null=True)

    def __str__(self):
        return self.name
