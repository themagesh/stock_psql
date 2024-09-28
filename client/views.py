from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .forms import InputDataForm
from .models import InputData


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

def success_view(request):
    stocks = InputData.objects.all()  # Query the InputData model
    context = {

        'stocks': stocks,  # Pass the fetched data to the template
    }
    return render(request, 'success.html', context)

# def singleLine(request):
#     stocks = InputData.objects.all()  # Query the InputData model
#     context = {
        
#         'stocks': stocks,  # Pass the fetched data to the template
#     }
#     return render(request, 'allstock.html', context)

def singleLine(request):
    stock_list = InputData.objects.all().order_by('id') # Fetch all stock records
    paginator = Paginator(stock_list,10)  # Show 10 stocks per pag
    page_number = request.GET.get('page')
    singleLine = paginator.get_page(page_number)

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
    # Handle AJAX request here
  # If it's an AJAX request, return only the new page content
        return render(request, 'allstock.html', {'singleLine': singleLine})
    return render(request, 'stocks.html', {'singleLine': singleLine})

         
