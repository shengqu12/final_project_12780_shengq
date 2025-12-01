from django.shortcuts import render, redirect
from django.db.models import F, Avg
from .models import CommunityGeo, ClimateRiskFactor, WeatherObs
import json
from datetime import datetime

from django.shortcuts import render, redirect
from django.db.models import F, Avg
from .models import CommunityGeo, ClimateRiskFactor

import json


def annotate_risk(qs):
    return qs.annotate(
        risk_score=(
            0.3 * F('flood_risk_score') +
            0.2 * F('storm_risk_score') +
            0.3 * F('heat_health_risk_coeff') +
            0.2 * (F('annual_high_temp_days') / 100.0)
        )
    )


def home(request):
    return redirect("climate:dashboard")


def dashboard(request):
    year = request.GET.get("year")
    month = request.GET.get("month")

    communities = CommunityGeo.objects.all().values(
        "community_id", "community_name", "latitude", "longitude"
    )

    comm_list = []

    for c in communities:
        risk_qs = ClimateRiskFactor.objects.filter(community_id=c["community_id"])
        if year:
            risk_qs = risk_qs.filter(year=int(year))
        if month:
            risk_qs = risk_qs.filter(month=int(month))

        risk_qs = annotate_risk(risk_qs)
        avg_risk = risk_qs.aggregate(avg_risk=Avg("risk_score"))["avg_risk"]
        avg_risk = float(avg_risk) if avg_risk is not None else 0.0

        comm_list.append({
            "id": c["community_id"],
            "name": c["community_name"],
            "lat": float(c["latitude"]),
            "lng": float(c["longitude"]),
            "avg_risk": avg_risk
        })

    communities_json = json.dumps(comm_list)

    return render(request, "climate/dashboard.html", {
        "communities_json": communities_json,
        "selected_year": year,
        "selected_month": month,
        "months": list(range(1, 12 + 1))
    })

def export_xlsx(request):
    import openpyxl
    from django.http import HttpResponse

    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "RiskFactors"
    headers = ["community_id", "year", "month", "Flood Risk", "Storm Risk", "Heat Health Risk"]
    ws.append(headers)

    records = ClimateRiskFactor.objects.order_by("community_id", "year", "month")
    for r in records:
        ws.append([r.community_id, r.year, r.month, r.flood_risk_score, r.storm_risk_score, r.heat_health_risk_coeff])

    response = HttpResponse(content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    response["Content-Disposition"] = 'attachment; filename="risk_factors.xlsx"'
    wb.save(response)
    return response
