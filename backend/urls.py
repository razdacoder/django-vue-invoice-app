from django.contrib import admin
from django.urls import path
from invoices import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/invoices/', views.invoice_list),
    path('api/v1/invoice/<str:uid>/', views.invoice),
]
