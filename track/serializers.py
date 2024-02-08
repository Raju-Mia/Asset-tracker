from rest_framework import serializers
from .models import *



# ==========Serializer for adding employees==============
class AddEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('name','phone','email','designation')


# ==========Serializer for adding assets==============
class AddAssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = '__all__'


# ==========Serializer for delegating assets to employees==============
class DelegateToSerializer(serializers.ModelSerializer):
    class Meta:
        model = DelegateTo
        fields = ('employee','assets','checked_out_at','condition')


# ==========Serializer for tracking when assets were given and returned==============
class WhenGiveAndReturnSerializer(serializers.ModelSerializer):
    model = serializers.StringRelatedField(read_only=True) # Read-only field to display related model's string representation.
    class Meta:
        model = GiveBack
        fields = ('asset_type','delegat','model','brand','checked_out_time','returned_date')



# ==========Serializer for give back assets==============
class WhenReturnSerializer(serializers.ModelSerializer):
    class Meta:
        model = GiveBack
        fields = ('asset_type','delegat','model','brand',)



# ==========Serializer for tracking conditions during asset delegation and return==============
class ConditionGiveAndReturnSerializer(serializers.ModelSerializer):
    model = serializers.StringRelatedField(read_only=True) # Read-only field to Display related model's string representation
    class Meta:
        model = GiveBack
        fields = ('employee_name','asset_type','model','brand','delegate_condition','returned_condition')