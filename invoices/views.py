from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Invoice, InvoiceItem
from .serializers import InvoiceSerializer, InvoicesSerializer

# Create your views here.


@api_view(['GET', 'POST'])
def invoice_list(request):
    if request.method == 'GET':
        invoices = Invoice.objects.all()
        serializer = InvoicesSerializer(invoices, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        invoice = Invoice(
            uid=request.data["uid"],
            from_address=request.data["from_address"],
            from_city=request.data["from_city"],
            from_zip_code=request.data["from_zip_code"],
            from_country=request.data["from_country"],
            client_name=request.data["client_name"],
            client_email=request.data["client_email"],
            client_address=request.data["client_address"],
            client_zip_code=request.data["client_zip_code"],
            client_city=request.data["client_city"],
            client_country=request.data["client_country"],
            invoice_date=request.data["invoice_date"],
            payment_due_date=request.data["payment_due_date"],
            terms=request.data["terms"],
            description=request.data["description"],
            status=request.data["status"],
        )
        invoice.save()
        for item in request.data['items']:
            invoice_item = InvoiceItem(
                invoice=invoice,
                name=item['name'],
                quantity=item['quantity'],
                price=item["price"]
            )
            invoice_item.save()
        return Response({"ok": True}, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def invoice(request, uid):
    try:
        invoice = Invoice.objects.get(uid=uid)
    except Invoice.DoesNotExist:
        return Response({"msg": "NOT FOUND", "ok": False}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = InvoiceSerializer(invoice, many=False)
        return Response(serializer.data)
    elif request.method == 'PATCH':
        invoice.status = request.data["status"]
        invoice.save()
        return Response({"msg": "Marked", "ok": True}, status=status.HTTP_202_ACCEPTED)
    elif request.method == 'PUT':
        invoice.from_address = request.data['from_address']
        invoice.from_city = request.data['from_city']
        invoice.from_zip_code = request.data['from_zip_code']
        invoice.from_country = request.data['from_country']
        invoice.client_name = request.data['client_name']
        invoice.client_email = request.data['client_email']
        invoice.client_address = request.data['client_address']
        invoice.client_city = request.data['client_city']
        invoice.client_zip_code = request.data['client_zip_code']
        invoice.client_country = request.data['client_country']
        invoice.payment_due_date = request.data['payment_due_date']
        invoice.terms = request.data['terms']
        invoice.description = request.data['description']
        invoice.save()
        for item in request.data['items']:
            invoice_item = InvoiceItem(
                invoice=invoice,
                name=item['name'],
                quantity=item['quantity'],
                price=item["price"]
            )
            invoice_item.save()
        return Response({"msg": "Updated", "ok": True}, status=status.HTTP_202_ACCEPTED)
    elif request.method == 'DELETE':
        invoice.delete()
        return Response({"msg": "Deleted", "ok": True}, status=status.HTTP_204_NO_CONTENT)
