from rest_framework import serializers
from .models import Vendor
from vendor.utils.unique_code import generate_vendor_code




class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ('id', 'name', 'vendor_code', 'contact_details', 'address')

    def create(self, validated_data):
        validated_data['vendor_code'] = generate_vendor_code()
        return super().create(validated_data)


# class PurchaseOrderSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PurchaseOrder
#         fields = '__all__'