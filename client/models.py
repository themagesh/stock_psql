from django.db import models
from django.utils import timezone

class InputData(models.Model):  # Ensure this line is correctly indented with no issues
    stockCode = models.CharField(max_length=100)  # Indent the fields inside the class
    companyName = models.CharField(max_length=40)
    industry = models.CharField(max_length=40)
    sector = models.CharField(max_length=40)
    website = models.URLField()
    about = models.CharField(max_length=5000)
    singleLine = models.URLField()
    upTrend = models.URLField()
    downTrend = models.URLField()
    lineTouch = models.URLField()
    lineCross = models.URLField()
    live_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    current_price = models.FloatField(default=0.0) 
    lastUpdated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.stockCode
class stock(models.Model):
    stockCode = models.CharField(max_length=100)
    companyName = models.CharField(max_length=40)
    industry = models.CharField(max_length=40)
    sector = models.CharField(max_length=40)
    website = models.URLField()
    about = models.CharField(max_length=5000)
    singleLine = models.URLField()
    upTrend = models.URLField()
    downTrend = models.URLField()
    lineTouch = models.URLField()
    lineCross = models.URLField()
    live_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    current_price = models.FloatField(default=0.0) 
    lastUpdated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.stockCode} - {self.companyName}"
    
