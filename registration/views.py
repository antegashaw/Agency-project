from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import EmployeeApplicationForm

# 1. ለዋናው ገጽ (Landing Page) የሚሆን ክፍል
def home_page(request):
    return render(request, 'registration/home.html')

# 2. ለፎርሙ መመዝገቢያ የሚሆን ክፍል
def apply_now(request):
    if request.method == 'POST':
        form = EmployeeApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'አፕሊኬሽንዎ በተሳካ ሁኔታ ተመዝግቧል! እናመሰግናለን።')
            return redirect('apply_now')
    else:
        form = EmployeeApplicationForm()
    
    return render(request, 'registration/apply.html', {'form': form})
