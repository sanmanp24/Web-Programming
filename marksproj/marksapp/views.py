from django.shortcuts import render,redirect

def pageone(request):
    if request.method=="POST":
        name=request.POST.get('name')
        marks=request.POST.get('marks')

        request.session['name']=name
        request.session['marks']=marks
        return redirect('pagetwo')
    return render(request,'pageone.html')
def pagetwo(request):
    name=request.session.get('name')
    marks=request.session.get('marks')
    if name and marks:
            cgpa=round(float(marks)/50,2)
    else:
        name='name'
        cgpa="N/A"
    if request.method=="POST":
        request.session.flush()
        return redirect('pageone')
    return render(request,'pagetwo.html',{'name':name,'cgpa':cgpa})