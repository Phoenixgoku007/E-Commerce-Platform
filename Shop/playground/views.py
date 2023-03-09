from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def say_hello(request):
    # return HttpResponse("Hello Arun") it directly prints the value
    
    x=1
    y=2

    return render(request,'hello.html',{'name':'Arun'}) # to pass templates and display on the browser