from django.db import models


class Vendor(models.Model):
    name = models.CharField(max_length=100)
    vendor_code = models.CharField(max_length=100,unique=True,blank=True, null=True)
    contact_details = models.TextField(max_length=150,blank=True,null=True)
    address = models.TextField(max_length=150,blank=True,null=True)
    
    def __str__(self) -> str:
        return self.name
    
    
class PurchaseOrder(models.Model):
    class StatusChoices(models.TextChoices):
        PENDING = 'pending', 'Pending'
        COMPLETED = 'completed', 'Completed'
        CANCELED = 'canceled', 'Canceled'   

    po_number = models.CharField(max_length=50, unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(
        max_length=10,
        choices=StatusChoices.choices,
        default=StatusChoices.PENDING
    )
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"PO {self.po_number} - {self.vendor.name}"