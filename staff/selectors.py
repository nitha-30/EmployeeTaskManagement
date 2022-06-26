from django.core.exceptions import ObjectDoesNotExist

from staff.models import Staff, StaffTaskManagement

def get_employee_using_id(id):
    try:
        staff_obj = Staff.objects.get(id=id)
        return True, staff_obj
    except ObjectDoesNotExist:
        return False, {}


def get_employee_task_using_id(id):
    try:
        task_obj = StaffTaskManagement.objects.get(id=id)
        return True, task_obj
    except ObjectDoesNotExist:
        return False, {}
