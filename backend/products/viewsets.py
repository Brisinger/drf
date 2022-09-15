from rest_framework import mixins, viewsets
from .models import Product
from .serializers import ProductSerializer


'''
get -> list -> QuerySet
get -> retrieve -> Product Instance Detail View
post -> create -> New Product Instance
put -> update-> Product Instance
patch -> partial_update -> Product attribute changed.
delete -> destroy -> Remove Product Instance
'''
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk' # Default


'''
get -> list -> QuerySet
get -> retrieve -> Product Instance Detail View
'''
class ProductGenericViewSet(
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin, 
        viewsets.GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk' # Default


product_list_view = ProductGenericViewSet.as_view({'get': 'list'})
product_detail_view = ProductGenericViewSet.as_view({'get', 'retrieve'})

