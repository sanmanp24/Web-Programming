from django.shortcuts import render
def register(request):
    if request.method=="POST":
        username=request.POST.get('username')
        if not username:
            return render(request,'register.html',{'error':'username required'})
        password=request.POST.get('password')
        email=request.POST.get('email')
        contact=request.POST.get('contact')
        return render(request,'success.html',{'username':username,'password':password,'email':email,'contact':contact})
    return render(request,'register.html')

