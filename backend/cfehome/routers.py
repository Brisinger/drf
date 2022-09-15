from rest_framework.routers import DefaultRouter
from products import viewsets 


router = DefaultRouter()
router.register(prefix='products', viewset=viewsets.ProductViewSet, basename='products')

#print(router.urls)
urlpatterns = router.urls # List of URL's pattern