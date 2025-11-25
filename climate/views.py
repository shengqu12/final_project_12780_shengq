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