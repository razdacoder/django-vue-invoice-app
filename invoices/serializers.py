from django.db import models
from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from .models import Invoice, InvoiceItem


class InvoicesSerializer(ModelSerializer):
    class Meta:
        model = Invoice
        fields = ['id', 'uid', 'status',
                  'client_name', 'payment_due_date', 'total']


class InvoiceItemSerializer(ModelSerializer):
    class Meta:
        model = InvoiceItem
        fields = "__all__"


class InvoiceSerializer(ModelSerializer):
    items = InvoiceItemSerializer(many=True)

    class Meta:
        model = Invoice
        fields = '__all__'
