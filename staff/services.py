import io
from django.conf import settings
import xlsxwriter
from datetime import date, timedelta

from staff.models import Staff, StaffTaskManagement

def create_employee_task(data):
    employee_task = StaffTaskManagement.objects.create(**data)
    return employee_task


def update_employee_task(task_object, data, user):
    data = dict(data)
    return StaffTaskManagement.objects.select_for_update().filter(
        id=task_object.id).update(**data, is_reviewed=True,
                                  reviewed_by=user)

def create_task_sheet():
    workbook = xlsxwriter.Workbook('media/employee_task_sheet.xlsx')
    worksheet = workbook.add_worksheet()
    bold = workbook.add_format({'bold': True})
    heading_array = ['ID', 'Employee Name', 'Email', 'Task', 'Date', 'Time taken', 'Comments']
    for col_num, heading in enumerate(heading_array):
        worksheet.write(0, col_num, heading, bold)
    today = date.today()
    start_date = date.today() - timedelta(days=7)
    tasks = StaffTaskManagement.objects.filter(created__date__gte=start_date,
                                               created__date__lte=today)
    for row_num, task in enumerate(tasks):
        column_data = [task.staff.id, task.staff.user.name, task.staff.user.email,
                        task.task, task.created.date().strftime('%d/%m/%Y'),
                        task.time_taken, task.comments]
        for col_num, data in enumerate(column_data):
            worksheet.write(row_num + 1, col_num, data)
            worksheet.set_column(row_num + 1, col_num, 25)
    workbook.close()
