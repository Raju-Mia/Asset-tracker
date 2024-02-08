from django.test import TestCase

from .models import Employee, Asset, DelegateTo, GiveBack
from .serializers import AddEmployeeSerializer, AddAssetSerializer, DelegateToSerializer, WhenGiveAndReturnSerializer, ConditionGiveAndReturnSerializer

# Create your tests here.


class SerializerTestCase(TestCase):
    def setUp(self):
        self.employee_data = {'name': 'Raju Mia', 'phone': '1234567890', 'email': 'rajumia@example.com', 'designation': 'Developer'}
        self.asset_data = {'asset_type': 'PHONE', 'model_no': 'X123', 'brand': 'Samsung'}
        self.employee = Employee.objects.create(**self.employee_data)
        self.asset = Asset.objects.create(**self.asset_data)

    # Add Employee
    def test_add_employee_serializer(self):
        serializer = AddEmployeeSerializer(instance=self.employee)
        self.assertEqual(serializer.data, self.employee_data)
