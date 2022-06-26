from django.db import models
from user.models import User


class Staff(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user.email}"


class StaffTaskManagement(models.Model):
    staff = models.ForeignKey("Staff", on_delete=models.CASCADE)
    task = models.CharField(max_length=200)
    time_taken = models.CharField(max_length=25,null=True, blank=True)
    comments = models.CharField(max_length=200, null=True, blank=True)
    is_reviewed = models.BooleanField(default=False)
    reviewed_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                    null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.staff.user.email}"