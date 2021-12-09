from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def venu(request,new):
    return render(request,'venu.html',{'new':new})

def base(request):
    return render(request,'base.html')

def child(request):
    return render(request,'child.html')

def parent(request):
    return render(request,'parent.html')

