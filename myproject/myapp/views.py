from django.shortcuts import render,redirect

def firstpage(request):
    if request.method=='POST':
        name=request.POST.get('name','')
        roll=request.POST.get('roll','')
        sub=request.POST.get('sub','')

        request.session['name']=name
        request.session['roll']=roll
        request.session['sub']=sub
        return redirect('secondpage')

    return render(request,'firstpage.html')

def secondpage(request):
    name=request.session.get('name','')
    roll=request.session.get('roll','')
    sub=request.session.get('sub','')
    context={
        'name':name,'roll':roll,'sub':sub
    }
    if request.method == 'POST':
        request.session.flush()
        return redirect('firstpage')
    return render(request,'secondpage.html',context)

