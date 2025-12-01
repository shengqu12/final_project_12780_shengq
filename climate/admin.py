from django.contrib import admin
from .models import CommunityGeo,WeatherObs,ClimateRiskFactor
# Register your models here.



admin.site.register(CommunityGeo)
admin.site.register(WeatherObs)


@admin.register(ClimateRiskFactor)
class ClimateRiskFactorAdmin(admin.ModelAdmin):
    list_display = ('community_id', 'year', 'month', 'annual_high_temp_days', 'flood_risk_score')
    list_filter = ('year', 'month')
    search_fields = ('community_id',)