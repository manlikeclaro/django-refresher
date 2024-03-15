from django.contrib import admin

from main_app.models import Report
admin.site.site_header = 'Politrack Africa'


# Register your models here.
class ReportAdmin(admin.ModelAdmin):
    list_display = ['id', 'report_name', 'release_date', 'created_at']
    search_fields = ['id', 'report_name']
    list_filter = ['report_name']


admin.site.register(Report, ReportAdmin)
