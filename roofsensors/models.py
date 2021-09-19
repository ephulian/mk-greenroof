from django.db import models

class ExperimentData(models.Model):
    recieved_at = models.DateTimeField(auto_now=True)
    green_roof_top = models.FloatField(null=True)
    green_roof_bottom = models.FloatField(null=True)
    control_top = models.FloatField(null=True)
    green_roof_middle = models.FloatField(null=True)
    control_bottom = models.FloatField(null=True)

    surface_heat_difference = models.FloatField(null=True) # control top - green middle
    bottom_difference = models.FloatField(null=True) # control bottom - green bottom

    moist_s0 = models.IntegerField(null=True)
    moist_s1 = models.IntegerField(null=True)

class AmbientData(models.Model):
    recorded_at = models.DateTimeField(null=True)
    red_one_humidity = models.FloatField(null=True)
    red_one_illumination = models.IntegerField(null=True)
    red_one_temperature = models.FloatField(null=True)

    red_two_humidity = models.FloatField(null=True)
    red_two_illumination = models.IntegerField(null=True)
    red_two_temperature = models.FloatField(null=True)

    red_three_humidity = models.FloatField(null=True)
    red_three_illumination = models.IntegerField(null=True)
    red_three_temperature = models.FloatField(null=True)
