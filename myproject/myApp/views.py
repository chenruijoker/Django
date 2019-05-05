from django.shortcuts import render,redirect
from django.db.models import Max,F,Q
import os
from django.conf import settings
from django.core.paginator import Paginator
from django.contrib.auth import logout

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from .models import Grades,Students,Text

def index(request):
    return HttpResponse("陈睿大宝贝！")

def details(request,num,num2):
    return HttpResponse("detail-%s-%s"%(num,num2))


def grades(request):
    gradeList=Grades.objects.all()
    return render(request,'myApp/grades.html',{"grades":gradeList})

def students(request):
    studentList=Students.stuObj2.all()
    return render(request,'myApp/student.html',{"students":studentList})


def gradestudent(request,num):
    grade=Grades.objects.get(pk=num)
    studentList=grade.students_set.filter(isDelete=False)
    print(type(grade.students_set))
    return render(request, 'myApp/student.html', {"students": studentList})



#下面为两种添加模式
def addstudent(request):
    grade=Grades.objects.get(pk=1)
    stu=Students.createStudent("陈dad",13,True,"I alw the BOSS",grade)
    stu.save()
    return HttpResponse("信息添加成功！")


def addstudent2(request):
    grade=Grades.objects.get(pk=1)
    #stu=Students.createStudent("陈瑞",23,True,"I am the BOSS",grade)

    stu=Students.stuObj2.createStudent("富人",23,True,"I am the BOSS",grade)
    stu.save()
    return HttpResponse("信息添加成功！")


#分页
def inquery(request,num):
    num = int(num)
    if num<1:
        num=1
    page=num
    if page<1:
        return HttpResponse("页面有误")
    stu = Students.stuObj2.all()[(page-1)*5:page*5]
    if len(stu)<1:
        return HttpResponse("无数据")
    else:
        print(request)
        return render(request, 'myApp/student.html', {"students": stu})

def inquery2(request):
    # 属性__方法=值就是语法了，除了contains还有startswith,endswith
    #如果方法前添加i则不区分大小写例如  sname__icontains
    #in 和contains类似
    #gte 大于等于，gt大于，lt 小于
    #stu=Students.stuObj2.filter(sage__contains=23)

    #stu=Students.stuObj2.filter(scontent__icontains='o')


    #联表查询
    #这句话是表述学生有人的简介里带o的  班级  是什么
    stu=Grades.objects.filter(students__scontent__contains='o')

    #求最大值，要引入包
    maxage=Students.stuObj2.aggregate(Max('sage'))
    print(maxage)

    #求比较表的某两个属性，也引入F对象包,甚至可以添加运算
    thegrade=Grades.objects.filter(ggirlnum__lt=F('gboynum')+20)
    print(thegrade)

    #查询具有或运算需求，引用Q对象包
    myresult=Students.stuObj2.filter(Q(sage=23) | Q(pk__gt=7))
    print(myresult)

    # 添加‘~’表示取反
    myresult = Students.stuObj2.filter(~Q(sage=23) | Q(pk__gt=7))
    print(myresult)

    return render(request, 'myApp/student.html', {"students": stu})


def myrequest(request):
    print(request.path)
    print(request.method)
    print(request.encoding)
    print(request.GET)
    print(request.POST)
    print(request.FILES)
    print(request.COOKIES)
    print(request.session)
    return HttpResponse("发送了请求")

def get1(request):
    a=request.GET.get('a')
    b = request.GET['b']
    c = request.GET.get('c')

    return HttpResponse(a+"-"+b+"-"+c)

def get2(request):
    a=request.GET.getlist('a') #允许get请求中a等于多个值
    a1 = a[0]
    a2 = a[1]
    c = request.GET.get('c')

    return HttpResponse(a1+"-"+a2+"-"+c)

def post1(request):
    return render(request, 'myApp/posttest.html')

def regist(request):
    name =request.POST.get("user")
    gender=request.POST.get("gender")
    pwd=request.POST.get("pwd")
    hobby=request.POST.getlist("hobby")
    print(name)
    print(gender)
    print(pwd)
    print(hobby)
    return HttpResponse("成功注册")

def showresponse(request):
    res=HttpResponse()
    res.content=b'show the content'
    print(res.content)
    print(res.charset)
    print(res.status_code)
    print(res._content-type)
    return res

def mycookie(request):
    res=HttpResponse()
    thecookie=request.COOKIES
    res.write("<h1>牛逼"+thecookie["mycookie"]+"</h1>")
    #res.set_cookie("mycookie","mytoken")
    return res

def redirect1(request):
    #return HttpResponseRedirect('redirect2/') 下面是第二种写法
    return redirect('redirect2/')
def redirect2(request):
    return HttpResponse("我是重定向后的提示")


def homepage(request):
    #获取session
    # username="游客"
    theusername=request.session.get("username","游客")#表示如果没取到，就是后面参数的值,这个是从mysql获取的
    #request.COOKIES['session_id']
    return render(request,'myApp/homepage.html',{'username':theusername})
def login(request):
    return render(request,'myApp/login.html')
def showhomepage(request):
    username=request.POST.get("username")
    #存储session
    request.session["username"]=username
    #设置session10秒后过期,不设置默认保存两周，如果是0则关闭浏览器失效，如果是None则永不过期
    #request.session.set_expiry(10)
    return redirect('homepage/')

#两种退出方式，其中一种需要导入包
def exitlogin(request):
    #logout(request)
    request.session.clear()
    #request.session.flush()
    return redirect('homepage/')



def tempshow(request):
    student=Students.stuObj2.all()

    return render(request,"myApp/mytemp.html",{"num":0,"stus":student,"shu1":1,"shu2":1,"str":"jojo","list":["A","B","C"]})

def thetemp2(request):
    return render(request,"myApp/base.html")
def thetemp3(request):
    return render(request,"myApp/thetempthree.html")

def mystatic(request):
    return render(request,"myApp/mystatc.html")

def savefile(request):
    #要先判断请求是否为post请求
    if request.method == "POST":
        f=request.FILES["file"]
        filePath=os.path.join(settings.MEDIA_ROOT,f.name)
        with open(filePath,'wb') as fp:
            #如果文件比较大，则采用分流去读
            for info in f.chunks():
                 fp.write(info)
        return HttpResponse("上传成功")
    else:
        return HttpResponse("上传失败")
def upfile(request):
    return render(request,"myApp/upfile.html")

#分页
def studentpage(request,pageid):
    allList=Students.stuObj2.all()
    paginator=Paginator(allList,4)
    currentPageList=paginator.page(pageid)
    limitpage = []
    pageid=int(pageid)
    limitpage = [pageid - 1, pageid, pageid + 1]
    if pageid <= paginator.num_pages and pageid >= paginator.num_pages-2:
        limitpage=[paginator.num_pages-2,paginator.num_pages-1,paginator.num_pages]
    if pageid >=0 and pageid <=3:
        limitpage=[x+1 for x in range(3)]
    if paginator.num_pages-1==pageid:
        limitpage = [pageid - 1, pageid, pageid + 1]





    #试试怎么自定义每次只显示几页？查看ssm分页思想
    return render(request,'myApp/studentpage.html',{"students":currentPageList,"limitpage":limitpage})

#ajax请求
def myajax(request):
    return render(request,'myApp/myAjax.html')

from django.http import JsonResponse

def getallstudentinfo(request):
    stus=Students.stuObj2.all()
    list=[]
    for stu in stus:
        list.append([stu.sname,stu.sage])
    return JsonResponse({"res":list})

#富文本
def tinymce(request):
    return render(request,'myApp/edit.html')
def savetinymce(request):
    content=request.POST.get('str')
    myedit=Text.createedit(content)
    print(myedit.str)
    myedit.save()
    return HttpResponse("存储成功")

