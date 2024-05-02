from django.urls import path
from .views import*

urlpatterns = [
    path('api/vendors/', VendorCreateAPIView.as_view(), name='vendor-create'),
    path('api/vendors/', VendorListAPIView.as_view(), name='vendor-list'),
    path('api/vendors/<uuid:pk>/', VendorRetrieveAPIView.as_view(), name='vendor-retrieve'),
    path('api/vendors/<uuid:pk>/', VendorUpdateAPIView.as_view(), name='vendor-update'),
    path('api/vendors/<uuid:pk>/', VendorDeleteAPIView.as_view(), name='vendor-delete'),
    path('api/purchase_orders/', PurchaseOrderCreateAPIView.as_view(), name='purchase-order-create'),
    path('api/purchase_orders/', PurchaseOrderListAPIView.as_view(), name='purchase-order-list'),
    path('api/purchase_orders/<uuid:pk>/', PurchaseOrderRetrieveAPIView.as_view(), name='purchase-order-retrieve'),
    path('api/purchase_orders/<uuid:pk>/', PurchaseOrderUpdateAPIView.as_view(), name='purchase-order-update'),
    path('api/purchase_orders/<uuid:pk>/', PurchaseOrderDestroyAPIView.as_view(), name='purchase-order-delete'),
    path('api/vendors/<uuid:pk>/performance/', VendorPerformanceAPIView.as_view(), name='vendor-performance'),
    path('api/purchase_orders/<uuid:pk>/acknowledge/', PurchaseOrderAcknowledgeAPIView.as_view(), name='purchase-order-acknowledge'),
]
