from django.urls import path
from . import views

urlpatterns = [
    path('input/', views.input_data_view, name='input-data'),
    path('success/', views.success_view, name='success'),  # Success page view
    path('stocks/', views.success_view, name='stock_list'),
    # path('register/', views.register, name='register')
]
