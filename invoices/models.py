from django.db import models
from django.utils.translation import deactivate

# Create your models here.

PAYMENT_TERMS = (
    ('30', '30 days'),
    ('60', '60 days')
)

STATUS = (
    ('paid', 'Paid'),
    ('pending', 'Pending'),
    ('draft', 'Draft')
)


class Invoice(models.Model):
    uid = models.CharField(default="", unique=True, max_length=50)
    from_address = models.CharField(max_length=50)
    from_city = models.CharField(max_length=50)
    from_zip_code = models.CharField(max_length=10)
    from_country = models.CharField(max_length=50)
    client_name = models.CharField(max_length=50)
    client_email = models.EmailField(unique=True, max_length=50)
    client_address = models.CharField(max_length=50)
    client_city = models.CharField(max_length=50)
    client_zip_code = models.CharField(max_length=10)
    client_country = models.CharField(max_length=50)
    invoice_date = models.DateField()
    payment_due_date = models.DateField()
    terms = models.CharField(choices=PAYMENT_TERMS,
                             default="", max_length=50)
    description = models.CharField(max_length=255)
    status = models.CharField(choices=STATUS, default=STATUS[1], max_length=50)
    total = models.FloatField(default="0.00")

    def __str__(self):
        return self.client_name + " Invoice"


class InvoiceItem(models.Model):
    invoice = models.ForeignKey(
        Invoice, related_name="items", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField(default="1")
    price = models.FloatField(default="0.00")
    total = models.FloatField(default="0.00")

    def __str__(self):
        return self.invoice.client_name + " " + self.name

    def save(self, *args, **kwargs):
        self.total = float(self.price) * int(self.quantity)
        self.invoice.total = float(self.invoice.total) + float(self.total)
        self.invoice.save()
        super(InvoiceItem, self).save(*args, **kwargs)
