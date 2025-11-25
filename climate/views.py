from django.shortcuts import render
from django.urls import reverse_lazy
from .models import ClimateRecord,Community
from .forms import ClimateRecordForm
from django.views.generic import CreateView, TemplateView, ListView, DetailView
# Create your views here.

class ClimateRecordCreateView(CreateView):
    model = ClimateRecord
    form_class = ClimateRecordForm
    template_name = "climate/record_form.html"
    success_url = reverse_lazy("climate:submit-success")


class SubmitSuccessView(TemplateView):
    template_name = "climate/submit_success.html"





from django.shortcuts import render
from django.db.models import Avg
from django.utils.dateparse import parse_date
import json

def dashboard(request):
    communities = Community.objects.all()
    comm_list = []
    for c in communities:
        avg_pollution = c.records.aggregate(avg=Avg("pollution_index"))["avg"]
        comm_list.append({
            "id": c.id,
            "name": c.name,
            "lat": float(c.latitude),
            "lng": float(c.longitude),
            "avg_pollution": avg_pollution or 0
        })
    context = {
        "communities_json": json.dumps(comm_list, default=str),
    }
    return render(request, "climate/dashboard.html", context)

from django.http import HttpResponse
import openpyxl
from openpyxl.utils import get_column_letter

def export_xlsx(request):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "ClimateRecords"
    headers = ["Community", "Borough", "Date", "Temperature", "Precipitation", "Pollution"]
    ws.append(headers)

    records = ClimateRecord.objects.select_related("community").order_by("community__name", "date")
    for r in records:
        ws.append([r.community.name, r.community.borough, r.date.isoformat(), r.temperature, r.precipitation, r.pollution_index])

    for i, _ in enumerate(headers, 1):
        ws.column_dimensions[get_column_letter(i)].width = 18

    response = HttpResponse(content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    response["Content-Disposition"] = 'attachment; filename="climate_records.xlsx"'
    wb.save(response)
    return response
