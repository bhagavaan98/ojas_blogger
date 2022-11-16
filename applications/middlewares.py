from django.http import HttpResponse
class ErrorMessageMiddleware(object):
    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self,request):
        response=self.get_response(request)
        return response

    def process_exception(self,request,exception):
        return HttpResponse(f'<h1>Currently we are facing some technical problems<br> The raised exception :{exception.__class__.__name__}<br>The exception message:{exception}</h1>')




   