from django.contrib import admin


# Register your models here.
from .models import Grades,Students,Text

admin.site.register(Text)



#还有StackedInline两者区别只有显示上的而已
class StudentsInfo(admin.TabularInline):
    model = Students
    extra = 2

class GradesAdmin(admin.ModelAdmin):
    #顺带添加学生
    inlines = [StudentsInfo]
    #列表页属性UI设定
    list_display = ['pk','gname','gdate','ggirlnum','gboynum','isDelete']
    list_filter = ['gname']
    search_fields = ['gname']
    list_per_page = 5

    # 添加修改页属性UI设定
    #fields,fieldsets不能同时使用
    #fields = ['ggirlnum','gboynum','gname','isDelete','gdate']
    fieldsets =[
        ("num",{"fields":['ggirlnum','gboynum']}),
        ("base", {"fields": ['gname', 'isDelete','gdate']}),
    ]

@admin.register(Students)
class StudentAdmin(admin.ModelAdmin):
    def gender(self):
        if self.sgender:
            return "男"
        else:
            return "女"
    list_display = ['pk','sname',gender,'sage','scontent','sgrade','isDelete']
    list_per_page = 5
    list_filter = ['sgrade']

    actions_on_bottom = True
    actions_on_top = False

admin.site.register(Grades,GradesAdmin)
# admin.site.register(Students,StudentAdmin) 可以在类上面用装饰器解决