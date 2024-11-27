from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class product(models.Model):
    cat=((1,'mobile'),(2,'cloths'),(3,'shoes'))
    name=models.CharField(max_length=50,verbose_name='Product Name')
    price=models.FloatField(verbose_name='Product Price')
    pdetails=models.CharField(max_length=50)
    cat=models.IntegerField(verbose_name='Product category',choices=cat)
    is_active=models.BooleanField(default=True,verbose_name='available')
    pimage=models.ImageField(upload_to='image')

    def __str__(self):
        return self.name
    
class carts(models.Model):
    uid=models.ForeignKey(User,on_delete=models.CASCADE,db_column="uid")
    pid=models.ForeignKey(product,on_delete=models.CASCADE,db_column="pid")
    qty=models.IntegerField(default=1)
class order(models.Model):
    order_id=models.CharField(max_length=50)
    uid=models.ForeignKey(User,on_delete=models.CASCADE,db_column="uid")
    pid=models.ForeignKey(product,on_delete=models.CASCADE,db_column="pid")
    qty=models.IntegerField(default=1)
