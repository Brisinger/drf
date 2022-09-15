from rest_framework import generics, mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response
#from django.http import Http404
from django.shortcuts import get_object_or_404
from api.mixins import (
    StaffEditorPermissionMixin, 
    UserQuerySetMixin)
from . models import Product
from . serializers import ProductSerializer


# Create your views here.
class ProductListCreateAPIView(
    UserQuerySetMixin,
    StaffEditorPermissionMixin, 
    generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    #permission_classes = [permissions.IsAdminUser, IsStaffEditorPermissions]

    def perform_create(self, serializer):
        # serializer.save(user = self.request.user)
        #print(f"Before removing email field {serializer.validated_data}")
        #email = serializer.validated_data.pop('email')
        #print(f"After removing email field {email}: {serializer.validated_data}")
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(user = self.request.user, content = content)

    # def get_queryset(self, *args, **kwargs):
    #     qs = super().get_queryset(*args, **kwargs)
    #     user = self.request.user
    #     if not user.is_authenticated:
    #         return Product.objects.none()
    #     #print(user)
    #     return qs.filter(user=user) 


class ProductDetailAPIView(
    UserQuerySetMixin,
    StaffEditorPermissionMixin, 
    generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    #allow_staff_view = True
    #permission_classes = [permissions.IsAdminUser, IsStaffEditorPermissions]
    # lookup_field = 'pk'

class ProductUpdateAPIView(
    UserQuerySetMixin,
    StaffEditorPermissionMixin, 
    generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    #authentication_classes = [authentication.SessionAuthentication]
    #permission_classes = [permissions.IsAdminUser, IsStaffEditorPermissions]
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title
        ## let's not save the serializer for now.

class ProductDestroyAPIView(
    UserQuerySetMixin,
    StaffEditorPermissionMixin, 
    generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    #authentication_classes = [authentication.SessionAuthentication]
    #permission_classes = [permissions.IsAdminUser, IsStaffEditorPermissions]
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        # instance
        super().perform_destroy(instance)

"""
Not going to use this class view.
"""
class ProductListAPIView(
    UserQuerySetMixin,
    generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk'

class ProductMixinView(
    UserQuerySetMixin,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin, 
    generics.GenericAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"

    def get(self, request, *args, **kwargs): #Http -> get
        print(args, kwargs)
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs): #Http -> post
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        # serializer.save(user = self.request.user)
        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(content = content)

"""
Function REST based API View. Create Retrieve and List.
"""
@api_view(["GET", "POST"])
def product_alt_view(request, pk=None, *args, **kwrags):
    method = request.method
    if method == "GET":
        if pk is not None:
            # url_args? -> lookup_field
            # get request -> Detail View
            obj = get_object_or_404(Product, pk = pk)
            data = ProductSerializer(obj, many = False).data
            return Response(data)
        # get request without URL lookup_field -> List View
        queryset = Product.objects.all()
        data = ProductSerializer(queryset, many = True).data
        return Response(data)
    if method == "POST":
        # Create View
        # serializer.save(user = self.request.user)
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid(raise_exception = True):
            print(serializer.validated_data)
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None
            if content is None:
                content = title
            serializer.save(content = content)
            return Response(serializer.data)
        return Response({"invalid": "Not good data"}, status = 400)
