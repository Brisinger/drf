from rest_framework import serializers
from rest_framework.reverse import reverse
from api.serializers import UserPublicSerializer 
from . models import Product
from . import validators



class ProductSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
            view_name='product-detail', 
            lookup_field='pk')
    edit_url = serializers.SerializerMethodField(read_only=True)
    title = serializers.CharField(validators=[validators.validate_title_no_hello,
       validators.unique_product_title])
    owner = UserPublicSerializer(source='user', read_only=True)

    class Meta:
       model = Product
       fields = [
        "owner",
        "title",
        'url',
        'edit_url',
        "content",
        "price", 
        "sale_price",
        "public",
       ]

    def get_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("product-detail", kwargs={'pk': obj.pk}, request=request)
    
    def get_edit_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse('product-update', kwargs={'pk': obj.pk}, request=request)
    