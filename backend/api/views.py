from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.models import Product
from products.serializers import ProductSerializer


"""
DRF Api View
"""
@api_view(["POST"])
def api_home(request, *args, **kwargs) -> Response:
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception = True):
        instance = serializer.save()
        return Response(ProductSerializer(instance).data)
    return Response({"invalid": "not good data"}, status=400)