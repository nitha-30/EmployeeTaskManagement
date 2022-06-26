from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser

from staff.selectors import (get_employee_using_id,
                             get_employee_task_using_id)
from staff.serializers import (StaffEmployeeTaskSerializer,
                               EmployeeTaskUpdateSerializer)
from staff.services import (create_employee_task,
                            update_employee_task)


class CreateTask(GenericAPIView):
    
    serilizer_class = StaffEmployeeTaskSerializer
    
    def post(self, request, *args, **kwargs):
        is_employee_exist, employee = get_employee_using_id(kwargs.get("staff_id"))
        serializer = self.serilizer_class(data=request.data)
        if serializer.is_valid():
            employee_task = create_employee_task(serializer.validated_data)
            return Response({"status": 0, "message": "Success", "task": employee_task.id})
        return Response({"status": -1, "errors": serializer.errors})


class ReviewTask(GenericAPIView):
    
    serilizer_class = EmployeeTaskUpdateSerializer
    permission_classes = (IsAdminUser, )
    
    def put(self, request, *args, **kwargs):
        is_task_exist, task = get_employee_task_using_id(kwargs.get("task_id"))
        serializer = self.serilizer_class(data=request.data)
        if serializer.is_valid():
            employee_task = update_employee_task(task, serializer.validated_data,
                                                 request.user)
            return Response({"status": 0, "message": "Success"})
        return Response({"status": -1, "errors": serializer.errors})
