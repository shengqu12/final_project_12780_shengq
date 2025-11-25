from django.urls import path
from .views import ClimateRecordCreateView, SubmitSuccessView,dashboard,export_xlsx

app_name = "climate"

urlpatterns = [
    path("submit/", ClimateRecordCreateView.as_view(), name="submit"),
    path("submit/success/", SubmitSuccessView.as_view(), name="submit-success"),
    path("dashboard/", dashboard, name="dashboard"),
    path("export/xlsx/", export_xlsx, name="export-xlsx"),


]