from rest_framework import serializers
from staff.models import Staff, StaffTaskManagement


class StaffEmployeeTaskSerializer(serializers.Serializer):
    staff = serializers.PrimaryKeyRelatedField(queryset=Staff.objects.all())
    comments = serializers.CharField(max_length=200, required=False, allow_null=True)
    task = serializers.CharField(max_length=200)


class StaffSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Staff
        fields = "__all__"


class EmployeeTaskUpdateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = StaffTaskManagement
        fields = "__all__"
    