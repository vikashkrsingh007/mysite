from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse("<html><body bgcolor=red><h1>welcome to mty 1st web page</h1></body></html>")
def wel(request):
    return HttpResponse("<html><head><title>1st web page</title></head><body bgcolor=green><h2>hello friend how are u</h2></body></html>")

# Create your views here.
