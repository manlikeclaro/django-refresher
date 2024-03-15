from django import forms

from main_app.models import Report


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = "__all__"
