from django.core.management import BaseCommand

from staff.services import create_task_sheet


class Command(BaseCommand):
    """
    Management command to create customer report
    """
    help = "Management command to create customer report"

    def handle(self, *args, **options):
        self.stdout.write("Start*****************")
        create_task_sheet()
        self.stdout.write("End*******************")
