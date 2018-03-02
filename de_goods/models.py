from django.db import models

# Create your models here.
class GoodInfo(models.Model):
    gtitle=models.CharField(max_length=50)
    gpic=models.ImageField(upload_to='de_goods')
    gprice=models.DecimalField(max_digits=5,decimal_places=2)
    isDelete=models.BooleanField(default=False)
    gunit=models.CharField(max_length=20,default='')
    gclick=models.IntegerField()
    gintro=models.CharField(max_length=200)
    # gdetial=HTMLField()
    gtype=models.ForeignKey('TypeInfo',None)
    gkuncun=models.IntegerField(default=0)
    gadv = models.BooleanField(default=False)

    def __str__(self):
        return self.gtitle

class TypeInfo(models.Model):
    title = models.CharField(max_length=20)
    scbz = models.BooleanField(default=False)
    pid = models.IntegerField(default=0)
    level = models.IntegerField(default=1)
    turl = models.CharField(max_length=64,default="")
    def __str__(self):
        return self.title
class GoodImage(models.Model):   #可以一个商品可以取多个图片的信息
    gid = models.ForeignKey("GoodInfo",None)
    lbsm = models.CharField(max_length=10,default="")
    sbpic = models.ImageField(upload_to="de_goods")
    lbpic = models.ImageField(upload_to="de_goods")
    def __str__(self):
        return self.lbsm