from rest_framework import serializers
from .models import Vendor , PurchaseOrder
from vendor.utils.unique_code import generate_vendor_code




class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ('id', 'name', 'vendor_code', 'contact_details', 'address')

    def create(self, validated_data):
        validated_data['vendor_code'] = generate_vendor_code()
        return super().create(validated_data)


class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = '__all__'
    
    def create(self, validated_data):
        validated_data['po_number'] = self.generate_po_number()
        return super().create(validated_data)
    
    def generate_po_number(self):
        import datetime
        today = datetime.date.today().strftime('%Y%m%d')
        last_po = PurchaseOrder.objects.filter(po_number__startswith=f'PO-{today}').last()
        if last_po:
            last_number = int(last_po.po_number.split('-')[-1])
            new_number = f'{last_number + 1:03d}'
        else:
            new_number = '001'
        return f'PO-{today}-{new_number}'
      
    def update(self, instance, validated_data):
        instance.po_number = validated_data.get('po_number', instance.po_number)
        instance.order_date = validated_data.get('order_date', instance.order_date)
        instance.delivery_date = validated_data.get('delivery_date', instance.delivery_date)
        instance.items = validated_data.get('items', instance.items)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.status = validated_data.get('status', instance.status)
        instance.quality_rating = validated_data.get('quality_rating', instance.quality_rating)
        instance.issue_date = validated_data.get('issue_date', instance.issue_date)
        instance.acknowledgment_date = validated_data.get('acknowledgment_date', instance.acknowledgment_date)
        
        instance.save()
        return instance
        