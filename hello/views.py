from django.http import HttpResponse

def hello(req):
    body = "Hello World"
    return HttpResponse(body)
