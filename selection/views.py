from django.shortcuts import render
from django.core.files import File
# Create your views here.
def details(request):
    return render(request,"choice.html")

def choices(request):
    if request.method=="POST":
        dict1=request.POST
        with open('choicesdata1.txt','w') as f:
            wrt=File(f)
            for key,value in dict1.items():
                wrt.write(key)
                wrt.write(value)
                wrt.write("\n")
    return render(request,"choice.html")

