from django.urls import path
from . import views

urlpatterns = [
    path('input/', views.input_data_view, name='input-data'),
    path('success/', views.success_view, name='success'), 
    path('singleLine/', views.singleLine, name='singleLine'),
    path('stock_price/', views.stock_prices_view, name='stock_prices_view'),
    path('home', views.home, name='home'),
    path('stock/<str:stock_code>/', views.stock, name='stock'), 
    path('search-stocks/', views.search_stocks, name='search_stocks'),
    
]


