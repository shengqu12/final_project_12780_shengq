from django.urls import path
from .views import dashboard, export_xlsx, home

app_name = "climate"

urlpatterns = [
    path('', home, name='home'),
    path('dashboard/', dashboard, name='dashboard'),
    path('export/', export_xlsx, name='export_xlsx'),
]
