from django.shortcuts import render
from django.core.files import File
# Create your views here.
def details(request):
    return render(request,'finder.html')

def finder1(request):
    if request.method=="POST":
        dict1=request.POST
        with open('finderdata.txt','w') as f:
            wrt=File(f)
            for key,value in dict1.items():
                wrt.write(key)
                wrt.write(" ")
                wrt.write(value)
                wrt.write("\n")
    wrt.close()
    return render(request,'finder.html')

