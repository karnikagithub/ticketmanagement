from email import message
from django.db import models

# Create your models here.

class UserModel(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    mobile = models.BigIntegerField()
    pwd = models.CharField(max_length=50)
    subject = models.CharField(max_length=100,null=True)
    message= models.TextField(null=True)
    status = models.CharField(default='pending',null=True,max_length=50)


    class Meta():
        db_table='user_register'


