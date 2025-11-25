from django.db import models

# Create your models here.

class Community(models.Model):
    name=models.CharField(max_length=100)
    borough=models.CharField(max_length=100,blank=True)
    latitude=models.DecimalField(max_digits=9,decimal_places=6)
    longitude=models.DecimalField(max_digits=9,decimal_places=6)

    def __str__(self):
        return self.name
    

class ClimateRecord(models.Model):
    community = models.ForeignKey(Community,on_delete=models.CASCADE,related_name='records')
    date= models.DateField()
    temperature = models.FloatField(null=True,blank=True)
    percipitation = models.FloatField(null=True,blank=True)
    pollution_index=models.IntegerField(null=True,blank=True)

    class Meta:
        ordering = ["-date"]
        unique_together = ('community','data')

    def __str__(self):
        return f"{self.community}-{self.date}"