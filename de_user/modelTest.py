from de_user.models import Address
#查询
add=Address.objects.all()     #获取所有地址
add=Address.objects.get(id=1,name='张三')   #获取指定字段的记录，可以加多个条件
adds2 = Address.objects.all().values_list('id','receiver') #过滤字段
adds2 = Address.objects.filter(id=1,receiver = 'zhangsan').all()    #符合过滤的所有记录
adds2 = Address.objects.filter(id=1,receiver = 'zhangsan').first()    #符合过滤的第一条记录
#新增
Address.objects.create(receiver = 'zhangsan',sheng='黑龙江') #新增一条jilu
#原版的新增
add4 = Address()
add4.receiver='wanngwu'
add4.save()
#删除
Address.objects.filter(receiver='zhangsan').delete()   #删除

#跟新
Address.objects.filter(receiver="zhangsan").update(receiver = "lisi")