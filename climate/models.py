from django.db import models

# Create your models here.    
class CommunityGeo(models.Model):
    community_id = models.CharField(max_length=20,primary_key=True)
    community_name = models.CharField(max_length=100)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    borough = models.CharField(max_length=100, blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    
    class Meta:
        db_table = 'community_geo'
        managed = False


class WeatherObs(models.Model):
    date = models.DateField(max_length=20, primary_key=True)
    community_id = models.CharField(max_length=20)

    PRCP = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    SNOW = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    SNWD = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    TAVG = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    TMAX = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    TMIN = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    TOBS = models.DecimalField(max_digits=6, decimal_places=2, null=True)

    class Meta:
        db_table = "weather_obs"
        managed = False      
        unique_together = ('date', 'community_id')   



class ClimateRiskFactor(models.Model):
    community_id = models.CharField(max_length=20,primary_key=True)
    year = models.IntegerField()
    month = models.IntegerField()
    annual_high_temp_days = models.IntegerField(null=True, blank=True)
    flood_risk_score = models.FloatField(null=True, blank=True)
    storm_risk_score = models.FloatField(null=True, blank=True)
    heat_health_risk_coeff = models.FloatField(null=True, blank=True)

    class Meta:
        db_table = 'climate_risk_factor'
        managed = False
        unique_together = ('community_id','year','month')
    def __str__(self):
        return f"{self.community_id}-{self.year}/{self.month}"
        

