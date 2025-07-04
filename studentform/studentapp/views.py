from django.shortcuts import render
from .forms import StudentForm

def student_view(request):
    form = StudentForm()
    result = ""
    percentage = None

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            total = data['english'] + data['physics'] + data['chemistry']+ data['SST'] + data['Arabic']
            percentage = round((total / 500) * 100, 2)
            result = (
                f"Name: {data['name']}\n"
                f"DOB: {data['dob']}\n"
                f"Address: {data['address']}\n"
                f"Contact: {data['contact']}\n"
                f"Email: {data['email']}\n"
                f"English: {data['english']} | Physics: {data['physics']} | Chemistry: {data['chemistry']} | SST:{data['SST']} | Arabic:{data['Arabic']}\n"
                f"Total Percentage: {percentage}%"
            )

    return render(request, 'studentapp/forms.html', {'form': form, 'result': result, 'percentage': percentage})
