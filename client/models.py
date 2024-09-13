from django.db import models

class InputData(models.Model):
    stockCode = models.CharField(max_length=4)
    companyName = models.CharField(max_length=40)
    industry = models.CharField(max_length=40)
    sector = models.CharField(max_length=40)
    website =  models.URLField()
    about = models.CharField(max_length=5000)
    singleLine =  models.URLField()
    upTrend =  models.URLField()
    downTrend =  models.URLField()
    lineTouch =  models.URLField()
    lineCross =  models.URLField()
    def __str__(self):
        return self.stockCode 
