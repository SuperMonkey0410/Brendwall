from django.urls import path
from .views import ProductListCreate, index


urlpatterns = [
    path('products/', ProductListCreate.as_view(), name='product-list-create'),
    path('', index, name='index'),  # Главная страница

]


# router = routers.DefaultRouter()
# router.register(r'product', ProductViewSet)
# urlpatterns = router.urls