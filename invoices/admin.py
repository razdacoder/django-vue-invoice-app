from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Invoice, InvoiceItem

# Register your models here.
admin.site.register(Invoice)
admin.site.register(InvoiceItem)
admin.site.unregister(User)
admin.site.unregister(Group)
