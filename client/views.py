from django.shortcuts import render, redirect
from .forms import InputDataForm


def input_data_view(request):
    if request.method == 'POST':
        form = InputDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect to a success page
    else:
        form = InputDataForm()
    
    return render(request, 'index.html', {'form': form})
def success_view(request):
    return render(request, 'success.html') 

