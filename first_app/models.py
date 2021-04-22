from django.db import models

class Weather(models.Model):
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    weather_f = models.FloatField()
    weather_c = models.FloatField()
    weather_t = models.CharField(max_length=255)
    weather_i = models.URLField()
    weather_h = models.FloatField()

