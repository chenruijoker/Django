from django.conf.urls import url
from . import  views
urlpatterns = [
    url(r'^$',views.index),
    url(r'^(\d+)/(\d+)$',views.details),
    url(r'^grade/$',views.grades),
    url(r'^student/$',views.students),
    url(r'^grade/(\d+)$',views.gradestudent),
    url(r'^addstudent/$',views.addstudent),
    url(r'^addstudent2/$',views.addstudent2),
    url(r'^inquery/(\d+)$',views.inquery),
    url(r'^inquery2/$',views.inquery2),
    url(r'^myrequest/$',views.myrequest),
    url(r'^get1/$',views.get1),
    url(r'^get2/$',views.get2),
    url(r'^post1',views.post1),
    url(r'^Regist',views.regist),
    url(r'^showresponse',views.showresponse),
    url(r'^cookietest',views.mycookie),
    url(r'^redirect1',views.redirect1),
    url(r'^redirect2',views.redirect2,name='ff'),
    url(r'^homepage',views.homepage),
    url(r'^login',views.login),
    url(r'^showhomepage',views.showhomepage),
    url(r'^exit',views.exitlogin),
    url(r'^temp',views.tempshow),
    url(r'^mytemp2',views.thetemp2),
    url(r'^mytemp3/$',views.thetemp3),
    url(r'^mystatic/$',views.mystatic),
    url(r'^savefile/$',views.savefile),
    url(r'^upfile/$',views.upfile),
    url(r'^studentpage/(\d+)/$',views.studentpage),
    url(r'^myajax/$',views.myajax),
    url(r'^getallstudentinfo/$',views.getallstudentinfo),
    url(r'^tinymce/$',views.tinymce),
    url(r'^savetinymce/$',views.savetinymce),

]