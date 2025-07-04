from django.shortcuts import render

def home(request):
    return render(request,'home.html')
def display(request):
    if request.method=='POST':
        manufacturer=request.POST.get('manufacturer')
        model=request.POST.get('model')
        phone=request.POST.get('phone')
        return render(request,'display.html',{'manufacturer':manufacturer,'model':model,'phone':phone})
