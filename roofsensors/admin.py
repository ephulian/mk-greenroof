from django.contrib import admin
from .models import ExperimentData, AmbientData

class AmbientAdmin(admin.ModelAdmin):
    list_display = (
        'recorded_at',
        'red_one_temperature',
        'red_one_humidity',
        'red_one_illumination',
        'red_two_temperature',
        'red_two_humidity',
        'red_two_illumination',
        'red_three_temperature',
        'red_three_humidity',
        'red_three_illumination')
    model = AmbientData

class ExperimentAdmin(admin.ModelAdmin):
    list_display = (
        'recieved_at',
        'green_roof_top',
        'green_roof_middle',
        'green_roof_bottom',
        'surface_heat_difference',
        'bottom_difference',
        'control_top',
        'control_bottom',
        'moist_s0',
        'moist_s1',)
    model = ExperimentData

admin.site.register(ExperimentData, ExperimentAdmin)
admin.site.register(AmbientData, AmbientAdmin)
