from django.contrib import admin
from django.urls import path
from .views import add_data, data_success  # Import the views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add/', add_data, name='add_data'),
    path('success/', data_success, name='data_success'),
]