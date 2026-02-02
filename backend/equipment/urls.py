from django.urls import path
from .views import upload_csv, get_history, generate_pdf

urlpatterns = [
    path('upload/', upload_csv),
    path('history/', get_history),
    path('report/', generate_pdf),
]
