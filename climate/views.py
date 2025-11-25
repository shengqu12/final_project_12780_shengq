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
