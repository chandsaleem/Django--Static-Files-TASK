from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    #return HttpResponse('<h1 style="color:pink">Hello World!</h1>')
    return render(request,'firstapp/index.html')

def about(request):
    return render(request, 'firstapp/about.html')

def Projects(request):
    return render(request, 'firstapp/Projects')
