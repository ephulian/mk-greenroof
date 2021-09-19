from django.db import models

class ExperimentData(models.Model):
    recieved_at = models.DateTimeField(auto_now=True)
    green_roof_top = models.DecimalField(max_digits=5, decimal_places=4, null=True)
    green_roof_bottom = models.DecimalField(max_digits=5, decimal_places=4, null=True)
    control_top = models.DecimalField(max_digits=5, decimal_places=4, null=True)
    green_roof_middle = models.DecimalField(max_digits=5, decimal_places=4, null=True)
    control_bottom = models.DecimalField(max_digits=5, decimal_places=4, null=True)
    moist_s0 = models.IntegerField()
    moist_s1 = models.IntegerField()

class AmbientData(models.Model):
    recorded_at = models.DateTimeField(null=True)
    red_one_humidity = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    red_one_illumination = models.IntegerField(null=True)
    red_one_temperature = models.DecimalField(max_digits=5, decimal_places=4, null=True)

    red_two_humidity = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    red_two_illumination = models.IntegerField(null=True)
    red_two_temperature = models.DecimalField(max_digits=5, decimal_places=4, null=True)

    red_three_humidity = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    red_three_illumination = models.IntegerField(null=True)
    red_three_temperature = models.DecimalField(max_digits=5, decimal_places=4, null=True)
