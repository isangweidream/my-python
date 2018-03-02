from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class User(models.Model):
    uname=models.CharField(max_length=20)
    upwd=models.CharField(max_length=40)
    uemil=models.EmailField(max_length=30,default='')
    urelname=models.CharField(max_length=20,default='')
    uadr=models.CharField(max_length=100,default='')
    uphone=models.CharField(max_length=11,default='')
    usex=models.CharField(max_length=1,default='')

class Address(models.Model):
    uid=models.IntegerField()  #相当于user这个表的主键
    receiver=models.CharField(max_length=20,help_text='收件人')
    sheng=models.CharField(max_length=8,default='')
    shi=models.CharField(max_length=16,default='')
    qu=models.CharField(max_length=16,default='')
    detialaddr=models.CharField(max_length=100,default='')
    rphone=models.CharField(max_length=11,default='0')
    yzbm = models.CharField(max_length=8,default='')
    mrdz=models.BooleanField(max_length=1,default=False)
    scbz=models.BooleanField(max_length=1,default=False)
