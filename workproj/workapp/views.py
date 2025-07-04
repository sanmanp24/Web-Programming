from django.shortcuts import render
from .models import Lives,Works
from .forms import CompanySearchForm,WorksForm
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome! Use /insert or /retrieve URLs</h1>")

def insert_data(request):
    if request.method=="POST":
        form=WorksForm(request.POST)
        if form.is_valid():
            form.save
            return render(request,'success.html',{'name':form.cleaned_data['person_name']})
        else:
            form=WorksForm()
        return render(request,'insert.html',{'form':form})
    
def retrieve_data(request):
    results=[]
    if request.method == 'POST':
        form = CompanySearchForm(request.POST)
        if form.is_valid():
            company_name = form.cleaned_data['company_name']
            works = Works.objects.filter(company_name=company_name)
            for w in works:
                try:
                    city = Lives.objects.get(person_name=w.person_name).city
                except Lives.DoesNotExist:
                    city = 'Unknown'
                results.append((w.person_name, city))
    else:
        form = CompanySearchForm()
    return render(request, 'retrieve.html', {'form': form, 'results': results})