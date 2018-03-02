from django.shortcuts import render
from de_goods.models import GoodInfo,TypeInfo
from django.core.paginator import Paginator,Page   #分页
from django.core import serializers
import json
# Create your views here.
#主页
def index(request):
    request.session['typeinfos']=typeinfos()
    # request.session["typeinfos"] =json.loads(serializers.serialize('json',TypeInfo.objects.filter(level__gt=1).all()))
    # request.session["typeinfos1"] =json.loads(serializers.serialize('json',TypeInfo.objects.filter(level=1).all()))
    context = {'guest_cart':1,'title':"首页"}

    #获取最火的四个商品
    hot = GoodInfo.objects.all().order_by("-gclick")[0:4]
    context.setdefault('hot',hot)
    #获取所有的类别
    typelist = TypeInfo.objects.all()
    for i in range(len(typelist)):
        typeinfo=typelist[i]
        # goods1=GoodInfo.objects.filter(gtype=typeinfo.id).order_by('-id')[0:4]
        goods1 = typeinfo.goodinfo_set.order_by('-id')[0:4]  #反向排序
        goods2 = typeinfo.goodinfo_set.order_by('-gclick')[0:4]
        context.setdefault('type'+str(i),goods1)
        context.setdefault('type'+str(i)+'-',goods2)
    print(context)


    return render(request,"index.html",context)

def typelist(request,tid,sid,pindex):


    typeinfo=TypeInfo.objects.get(pk = int(tid))
    typeinfos  = TypeInfo.objects.filter(level__gt=1).all()
    typeinfos1  = TypeInfo.objects.filter(level=1).all()
    news = typeinfo.goodinfo_set.order_by('-id')[0:2]
    ordby = "-id" if sid=='1' else '-gprice' if sid=='2' else '-glick'      #比较骚的地下的简写
    # if sid == "1":
    #     good_list = typeinfo.goodinfo_set.order_by("-id")
    # elif sid == "2":
    #     good_list = typeinfo.goodinfo_set.order_by("-gprice")
    # elif sid == "3":
    #     good_list = typeinfo.goodinfo_set.order_by('-gclick')
    ssnr = request.GET.get('ssnr','').strip()
    if ssnr:
        good_list = GoodInfo.objects.filter(gtitle__contains=ssnr)
    else:
        good_list=typeinfo.goodinfo_set.order_by(ordby)
    paginator = Paginator(good_list,5)  #每页共有10条数据
    page = paginator.page(int(pindex))  #取第几页

    context = {'title':"商品列表",'guest_cart':1,'page':page,
               'paginator':paginator,'typeinfo':typeinfo,
               'sort':sid,'news':news,'typeinfos':typeinfos,'typeinfos1':typeinfos1,'ssnr':ssnr}
    return render(request, 'de_goods/list.html', context)





# def typeinfos(tjson=[]):       #所有的分类级别都可以直接往里写
#     if tjson:
#         for i in tjson:
#             if 'sub' not in i: i['sub'] = []
#             subtype= json.loads(serializers.serialize('json',TypeInfo.objects.filter(pid=i['pk']).all()))
#             for j in subtype:
#                 i['sub'].append(j)
#             if i['sub']:typeinfos(i['sub'])
#     else:
#         tjson = json.loads(serializers.serialize('json',TypeInfo.objects.filter(pid=0).all()));
#         typeinfos(tjson)
#     return tjson

def typeinfos(tjson=[],ts=None):
    for i in tjson:
        i['sub']=[j for j in ts if j['fields']['pid']==i['pk']]
        if i['sub']:typeinfos(i['sub'],ts)
    if len(tjson)==0:
        ts=json.loads(serializers.serialize('json',TypeInfo.objects.all()))
        tjson=[i for i in ts if i['fields']['pid']==0]                #列表生成式
        typeinfos(tjson,ts)
    return tjson
