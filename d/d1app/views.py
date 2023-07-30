from django.http import HttpResponse

def index(request):
    return HttpResponse('helo')

def index2(request):
    return HttpResponse('vay')