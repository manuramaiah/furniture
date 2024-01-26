from django.shortcuts import render

from .models import Furniture
# Create your views here.
def index(request):
    obj=Furniture.objects.all()
    return render(request,'index.html',{'result':obj})
def about(request):
    return render(request,'about.html')
def blog(request):
    return render(request,'blog.html')
def contact(request):
    return render(request,'contact.html')
def furniture(request):
    return render(request,'furniture.html')
