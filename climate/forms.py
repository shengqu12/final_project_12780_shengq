from django import forms
from .models import ClimateRecord

class ClimateRecordForm(forms.ModelForm):
    class Meta:
        model = ClimateRecord
        fields = ["community", "date", "temperature", "precipitation", "pollution_index"]
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
        }

    def clean_date(self):
        date = self.cleaned_data["date"]
        from django.utils import timezone
        if date > timezone.now().date():
            raise forms.ValidationError("Date cannot be in the future.")
        return date
