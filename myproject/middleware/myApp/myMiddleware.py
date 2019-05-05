from django.utils.deprecation import MiddlewareMixin

class MyMiddle(MiddlewareMixin):
    def process_request(self,request):
        print("get请求获得的对象为：",request.GET.get("a"))

