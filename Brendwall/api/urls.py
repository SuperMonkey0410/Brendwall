from django.urls import path
from .views import ProductListCreate,ProductDetail, index


urlpatterns = [
    path('products/', ProductListCreate.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product-detail'),  # URL для получения товара по ID
    path('', index, name='index'),  # Главная страница

]