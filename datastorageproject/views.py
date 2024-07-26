from django.shortcuts import render, redirect
from .models import Data
from .forms import DataForm

def add_data(request):
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            new_data = Data(name=name)
            new_data.save()
            return redirect('data_success')
    else:
        form = DataForm()
    return render(request, 'add_data.html', {'form': form})

def data_success(request):
    return render(request, 'data_success.html')
