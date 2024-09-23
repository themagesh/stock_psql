from django.urls import path
from . import views

urlpatterns = [
    path('input/', views.input_data_view, name='input-data'),
    path('success/', views.success_view, name='success'),  # Success page view
    path('singleLine/', views.singleLine, name='ssingleLine'),
    # path('register/', views.register, name='register')
]
