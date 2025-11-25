from django.urls import path
from .views import ClimateRecordCreateView, SubmitSuccessView

app_name = "climate"

urlpatterns = [
    path("submit/", ClimateRecordCreateView.as_view(), name="submit"),
    path("submit/success/", SubmitSuccessView.as_view(), name="submit-success"),
]