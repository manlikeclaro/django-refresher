from django.db import models


# Create your models here.
class Report(models.Model):
    report_name = models.CharField(max_length=256)
    file_name = models.FileField(upload_to='reports', null=True)
    release_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.report_name}'
