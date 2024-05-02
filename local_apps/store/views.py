from django.shortcuts import render
from .serializers import *
from .models import*
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Vendor
from django.db.models import Avg, ExpressionWrapper, F, DurationField,Count
from django.utils import timezone
from django.db.models.functions import Coalesce
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class VendorCreateAPIView(generics.CreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    permission_classes = [IsAuthenticated]
  

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class VendorListAPIView(generics.ListAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    permission_classes = [IsAuthenticated]


class VendorRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'


class VendorUpdateAPIView(generics.UpdateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'



class VendorDeleteAPIView(generics.DestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)



class PurchaseOrderCreateAPIView(generics.CreateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    permission_classes = [IsAuthenticated]

class PurchaseOrderListAPIView(generics.ListAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        vendor_id = self.request.query_params.get('vendor')
        if vendor_id:
            queryset = queryset.filter(vendor=vendor_id)
        return queryset

class PurchaseOrderRetrieveAPIView(generics.RetrieveAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'

class PurchaseOrderUpdateAPIView(generics.UpdateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'

class PurchaseOrderDestroyAPIView(generics.DestroyAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'
    
    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class VendorPerformanceAPIView(generics.RetrieveAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorPerformanceSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'
    
class PurchaseOrderAcknowledgeAPIView(generics.UpdateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'
    

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        # Calculate on-time delivery rate
        if instance.status == 'completed' and instance.delivery_date <= instance.acknowledgment_date:
            vendor = instance.vendor
            completed_orders_count = PurchaseOrder.objects.filter(vendor=vendor, status='completed').count()
            on_time_delivery_count = PurchaseOrder.objects.filter(vendor=vendor, status='completed', delivery_date__lte=F('acknowledgment_date')).count()

            if completed_orders_count > 0:
                vendor.on_time_delivery_rate = on_time_delivery_count / completed_orders_count
            else:
                vendor.on_time_delivery_rate = 0.0
        if instance.status == 'completed' and instance.quality_rating is not None:
            vendor = instance.vendor
            quality_rating_avg = PurchaseOrder.objects.filter(vendor=vendor, quality_rating__isnull=False).aggregate(avg_quality_rating=Avg('quality_rating'))['avg_quality_rating'] or 0.0
            vendor.quality_rating = quality_rating_avg
        if instance.acknowledgment_date is not None:
            vendor = instance.vendor
            response_time_avg = PurchaseOrder.objects.filter(vendor=vendor, acknowledgment_date__isnull=False).annotate(
                response_time=ExpressionWrapper(F('acknowledgment_date') - F('issue_date'), output_field=DurationField())
            ).aggregate(avg_response_time=Avg('response_time'))['avg_response_time']
            vendor.response_time = response_time_avg
        vendor = instance.vendor
        total_orders_count = PurchaseOrder.objects.filter(vendor=vendor).count()
        fulfilled_orders_count = PurchaseOrder.objects.filter(vendor=vendor, status='completed').count()

        if total_orders_count > 0:
            vendor.fulfillment_rate = fulfilled_orders_count / total_orders_count
        else:
            vendor.fulfillment_rate = 0.0
            vendor.save()

        return Response(serializer.data)