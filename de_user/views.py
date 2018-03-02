from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,JsonResponse

from hashlib import sha1
from de_user.models import User,Address
from de_goods.models import GoodInfo
from de_user import user_decorator

# Create your views here.
def login(request):
    uname=request.COOKIES.get('uname','')
    pwd=request.COOKIES.get('upwd','')
    context={'uname':uname,
             'pwd':pwd,
             'error':0}
    try:
        url = request.META['HTTP_REFERER']
        if url == "http://127.0.0.1:8000/user/reg":
            url = '/'
        else:
            pass

    except:url='/'
    response=render(request,'de_user/login.html',context)
    response.set_cookie('url',url)
    return response

def register(request):
    return render(request,'de_user/register.html')
def login_handle(request):
    post=request.POST#接受表单请求
    uname=post.get('username')
    pwd=post.get('pwd')
    remember=post.get('remember','0')
    s=sha1()
    s.update(pwd.encode('utf8'))   #先编码
    upwd=s.hexdigest()
    #mysql语句，游标获取关闭，提交一条信息
    user=User.objects.filter(uname=uname).filter(upwd=upwd).first()
    if user:
        url=request.COOKIES.get('url','/')  #根目录
        red=HttpResponseRedirect(url)
        #1将保存几天，否则只保存一瞬间   浏览器里面
        if remember=='1':
            red.set_cookie('uname',uname)
            red.set_cookie('upwd',pwd)
            red.set_cookie('uname',uname.encode('utf-8')) #存在浏览器里

        else:
            red.set_cookie('uname','',max_age=-1)
            red.set_cookie('upwd','',max_age=-1)
            #服务器里保存  半小时
        request.session['username']=uname
        request.session['uid']=user.id
        return red
    else:
        context={'error':1,'uname':uname}
        return render(request,'de_user/login.html',context)  #成功进入首页否则还在原页面
def register_handle(request):
    post=request.POST
    uname=post.get('username','')
    pwd=post.get('pwd','')
    cpwd=post.get('cpwd','')
    uemail=post.get('email','')

    if pwd !=cpwd:
        return redirect('/user/reg')
    s1=sha1()
    s1.update(pwd.encode('utf8'))
    pwd=s1.hexdigest()
    user=User()  #存入数据库
    user.uname=uname
    user.upwd=pwd
    user.uemil=uemail
    user.save()
    return redirect('/user/login')

def logout(request):
    request.session.flush()
    return redirect('/')

def register_exist(request):
    uname=request.GET.get('un')
    count=User.objects.filter(uname=uname).count()
    return JsonResponse({'count':count})
@user_decorator.login
def shdz(request):

    adds=Address.objects.filter(uid=request.session.get('uid',''),scbz=0)
    return render(request,'de_user/user_address.html',locals())

@user_decorator.login    #加一些过滤条件，比如没有登录不能进入别的界面
def user_center(request):
    return  render(request,'de_user/user_center.html',locals())
def zhanghuguanli(request):
    return  render(request,'de_user/user_account.html',locals())

def user_center_info(request):
    username=request.session.get('username','')
    user=User.objects.filter(uname=username).first()
    goodids=request.COOKIES.get('goodids','')
    goods_list=[]
    if goodids !='':
        goodids=goodids.split(',')
        for i in goodids:
            goods_list.append(GoodInfo.objects.filter(pk=i).first())
            pass
    return render(request,'de_user/user_account.html',locals())

def userupdate(request):
    post=request.POST
    uid=request.session.get('uid','')
    user=User.objects.filter(id=uid).first()
    user.uname=post.get('un','')
    user.urelname=post.get('urn','')
    user.uphone=post.get('uphone','')
    user.uemail=post.get('uemil','')
    user.usex=post.get('usex','')
    user.save()
    request.session['username']=user.uname
    return redirect('/')
@user_decorator.login
def save_addr(request):
    post=request.POST
    aid = post.get("aid")
    if aid:
        Address.objects.get(id=aid).update(receiver=post.get('receiver'),sheng=post.get('sheng'),rphone=post.get('rphone'),shi=post.get('shi'),qu=post.get('qu'),detialaddr = post.get('detialaddr'),yzbm=post.get('yzbm'))
    else:
        Address.objects.create(receiver=post.get('receiver'),sheng=post.get('sheng'),rphone=post.get('rphone'),shi=post.get('shi'),qu=post.get('qu'),detialaddr = post.get('detialaddr'),yzbm=post.get('yzbm'),uid=request.session["uid"])
    # uid=request.session.get('uid','')
    # add=Address()
    # add.uid = uid
    # add.receiver=post.get('receiver','')
    # add.sheng=post.get('sheng','')
    # add.rphone=post.get('rphone','')
    # add.shi=post.get('shi','')
    # add.qu=post.get('qu','')
    # add.yzbm=post.get('yzbm','')
    # add.detialaddr = post.get('detialaddr')
    # add.save()
    return render('de_user/user_address.html')
def mrdz(request):
    dzid=request.GET.get('dzid')
    Address.objects.all().update(mrdz=0)
    add=Address.objects.filter(id=dzid).update(mrdz = 1)
    return redirect('/user/shdz')
@user_decorator.login
def scdz(request):
    dzid=request.GET.get('dzid')
    # Address.objects.all().update(scbz=0)
    Address.objects.filter(id=dzid).update(scbz=1)
    return redirect('/user/shdz')
@user_decorator.login
def bjdz(request):
    dzid=request.GET.get('dzid')
    add=Address.objects.get(id=dzid,scbz=0)
    adds=Address.objects.filter(uid=request.session.get('uid',''),scbz=0)
    return render(request,'de_user/user_address.html',locals())

def detail(request):
    return  render(request,'de_goods/detailsp.html.html',locals())


