from django.db import models
from local_apps.main.models import Main
import uuid
# Create your models here.

class Vendor(Main):
    name = models.CharField(blank=True,null=True,max_length=255)
    contact_details = models.TextField(blank=True,null=True)
    address = models.TextField(blank=True,null=True)
    vendor_code = models.CharField(blank=True,null=True,max_length=255,editable=False)   
    on_time_delivery_rate = models.FloatField(blank=True,null=True)
    quality_rating_avg = models.FloatField(blank=True,null=True)
    average_response_time= models.FloatField(blank=True,null=True)
    fulfillment_rate= models.FloatField(blank=True,null=True)

    def generate_unique_vendor_code(self):
        # Generate a unique vendor code using a combination of "VD" and a random string
        return f"VD_{uuid.uuid4().hex}"

    def save(self, *args, **kwargs):
        if not self.vendor_code:
            self.vendor_code = self.generate_unique_vendor_code()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.vendor_code if self.vendor_code else "No Name"

    class Meta:
        ordering = ["-created_at", "-updated_at"]
        verbose_name = "Vendor"
        verbose_name_plural = "Vendores"



class PurchaseOrder(Main):
    po_number = models.CharField(blank=True,null=True,max_length=255,editable=False)
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, blank=True, null=True,related_name='store_purchase_order_vendor')
    order_date = models.DateTimeField(blank=True,null=True)
    delivery_date = models.DateTimeField(blank=True,null=True)
    items = models.JSONField(blank=True,null=True)
    quantity = models.IntegerField(blank=True,null=True)
    status = models.CharField(blank=True,null=True,max_length=255)
    quality_rating = models.FloatField(blank=True,null=True)
    issue_date = models.DateTimeField(blank=True,null=True)
    acknowledgment_date = models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return self.po_number if self. po_number else "No Ponumber"

    def generate_unique_po_number(self):
        # Generate a unique ID using a combination of "po" and current timestamp
        return f"po_{uuid.uuid4().hex}"

    def save(self, *args, **kwargs):
        if not self.po_number:
            self.po_number = self.generate_unique_po_number()
        super().save(*args, **kwargs)


    class Meta:
        ordering = ["-created_at", "-updated_at"]
        verbose_name = "PurchaseOrder"
        verbose_name_plural = "PurchaseOrders"






class HistoricalPerformance(Main):
    vendor =  models.ForeignKey(Vendor, on_delete=models.SET_NULL, blank=True, null=True,related_name='store_historical_performance_vendor')
    date = models.DateTimeField(blank=True,null=True)
    on_time_delivery_rate = models.FloatField(blank=True,null=True)
    quality_rating_avg = models.FloatField(blank=True,null=True)
    average_response_time = models.FloatField(blank=True,null=True)
    fulfillment_rate = models.FloatField(blank=True,null=True)

    def __str__(self):
        return self.vendor if self.vendor else "No Vendor"



    class Meta:
        ordering = ["-created_at", "-updated_at"]
        verbose_name = "HistoricalPerformance"
        verbose_name_plural = "HistoricalPerformances"


    

