from django.views.decorators.http import require_GET
from django.http import JsonResponse
from django.shortcuts import render, redirect,get_object_or_404
from django.utils.timezone import now
from django.core.paginator import Paginator
from .forms import InputDataForm
from .models import InputData
import yfinance as yf
from django.core.management import call_command
from django.http import HttpResponse


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
    stocks = InputData.objects.all()  # Query the InputData model
    context = {

        'stocks': stocks,  # Pass the fetched data to the template
    }
    return render(request, 'success.html', context)

def singleLine(request):
    stock_list = InputData.objects.all().order_by('id') # Fetch all stock records
    paginator = Paginator(stock_list,10) # Show 10 stocks per pag
    print(stock_list.count()) 
    page_number = request.GET.get('page',1)
    singleLine = paginator.get_page(page_number)

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':# Handle AJAX request here
         if not singleLine.has_next():
            return render(request, 'allstock.html', {'singleLine': []})
         return render(request, 'allstock.html', {'singleLine': singleLine})
    return render(request, 'stocks.html', {'singleLine': singleLine})

         
def home(request):
    return render(request, 'stock/home.html')

def about(request):
    return render(request, 'stock/about.html')



def stock_prices_view(request):
    # List of stock codes you want to fetch
    stocks = InputData.objects.all()
    stock_data_list = []

    for stock in stocks:
        ticker = f"{stock.stockCode}.NS"  # Ensure you use the correct format for Yahoo Finance

        # Fetch the ticker data
        stock_ticker = yf.Ticker(ticker)
        try:
            # Fetch live price for each stock using yfinance
            current_price = stock_ticker.history(period='1d')['Close'].iloc[-1]  # Latest price
            last_updated = now()  # Record current timestamp
        except Exception as e:
            current_price = 'N/A'  # Handle error, no price available
            last_updated = 'N/A'  # No update time in case of error
        
        stock_data_list.append({
            'stock_code': stock.stockCode,
            'company_name': stock.companyName,
            'current_price': current_price,
            'last_updated': last_updated.strftime('%b. %d, %Y, %I:%M %p') if last_updated != 'N/A' else 'N/A',
            'previousClos':stock_ticker.info.get('previousClose','N/A'),
        })
    
    context = {
        'stock_data_list': stock_data_list
    }

    return render(request, 'stock_prices.html', context)

def stock(request, stock_code):
    stock = get_object_or_404(InputData, stockCode=stock_code)
    return render(request, 'stock.html', {'stock': stock})

