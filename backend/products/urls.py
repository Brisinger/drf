"""
products URL Configuration
"""
from django.urls import path
from products import views


# /api/products/
urlpatterns = [
    path('', views.ProductListCreateAPIView.as_view(), name='product-list'),
    path('<int:pk>/update/', views.ProductUpdateAPIView.as_view(), name='product-update'), # endpoint /api/products/{pk}/update/
    path('<int:pk>/delete/', views.ProductDestroyAPIView.as_view()), # endpoint /api/products/{pk}/delete/
    path('<int:pk>/', views.ProductDetailAPIView.as_view(), name='product-detail'), # endpoint /api/products/{pk}/
]