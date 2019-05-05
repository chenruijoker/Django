from django.db import models

# Create your models here.
class Grades(models.Model):
    """
    本函数用于分数表
    """
    gname   =models.CharField(max_length=20,db_column='thename')
    gdate   =models.DateTimeField()
    ggirlnum=models.IntegerField()
    gboynum =models.IntegerField()
    isDelete=models.BooleanField(default=False)
    isGoodgrade = models.BooleanField(default=False)#新增字段
    def __str__(self):
        return self.gname
    class Meta:
        #定义表名
        db_table="grades"
        #定义排序正序，倒序改成   '-id'
        ordering=['id']



#自定义模型管理器,进行筛选
class StudentManager(models.Manager):
    def get_queryset(self):
        return super(StudentManager, self).get_queryset().filter(isDelete=False)
    def createStudent(self,name,age,gender,content,grade,isD=False):
        stu=self.model()
        #print(type(grade))
        stu.sname=name
        stu.sage=age
        stu.sgender=gender
        stu.sgrade=grade
        return stu



class Students(models.Model):
    """
    本函数用于学生信息表
    """
    #自定义模型管理器，这样objects就会失效，并被stuObj取代
    stuObj=models.Manager()
    stuObj2=StudentManager()

    sname   =models.CharField(max_length=20,db_column='studentname')
    sgender =models.BooleanField(default=True)
    sage    =models.IntegerField()
    scontent=models.CharField(max_length=100)
    isDelete=models.BooleanField(default=False)
    sgrade  =models.ForeignKey("Grades")
    def __str__(self):
        return self.sname

    class Meta:
        db_table='student'
        ordering=['id']

    #实现增加数据，定义一个类方法创建对象,下面的注解表示这个方法是类方法
    @classmethod
    def createStudent(cls,name,age,gender,content,grade,isD=False):
        stu=cls(sname=name,sage=age,sgender=gender,scontent=content,sgrade=grade,isDelete=isD)
        return stu


    #如果不用@classmethod 那么书写如下
    #def createStudent(Students): 对，就是使用本类类名

from tinymce.models import HTMLField
class Text(models.Model):
    str=HTMLField()
    @classmethod
    def createedit(cls,thestr):
        edittiny=cls(str=thestr)
        return edittiny





