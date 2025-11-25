from django.contrib import admin
from .models import Community, ClimateRecord
# Register your models here.

@admin.register(Community)
class CommunityAdmin(admin.ModelAdmin):
    list_display = ('name','borough','latitude','longitude')
    search_fields=('name','borough')

@admin.register(ClimateRecord)
class ClimateRecordAdmin(admin.ModelAdmin):
    list_display = ("community", "date", "temperature", "precipitation", "pollution_index")
    list_filter = ("community", "date")
    search_fields = ("community__name",)