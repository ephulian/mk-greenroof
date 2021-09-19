import json
from django.views.generic import View
from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from roofsensors import converter
from .models import ExperimentData, AmbientData
import string

from datetime import datetime

@method_decorator(csrf_exempt, name='dispatch')
class SensorDataView(View):
    def post(self, request):
        try:
            data = json.loads(request.body.decode('utf-8'))
            print(data)
            #new_data = ExperimentData()
            #new_data.save()
            return JsonResponse({'response':'success'})
        except:
            return JsonResponse({'response':'error'})


@method_decorator(csrf_exempt, name='dispatch')
class AmbientSensorDataView(View):
    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))

        for device_id, data in data.items():
            for l in data:
                timestamp = l['timestamp']
                value = l['value']

                if set(value).issubset(string.hexdigits):
                    new_data = AmbientData()
                    new_data.recorded_at = datetime.strptime( timestamp, "%Y-%m-%d_%H:%M:%S" )

                    # Valid hex so convert
                    object = converter.SensorDataConverter(device_id, value)
                    device_locaiton, device_name = object.sensor_location()

                    if device_name == "Red 1":
                        new_data.red_one_temperature = object.temp_range()
                        new_data.red_one_humidity = object.hum_range()
                        new_data.red_one_illumination = object.illum_range()
                    elif device_name == "Red 2":
                        new_data.red_two_temperature = object.temp_range()
                        new_data.red_two_humidity = object.hum_range()
                        new_data.red_two_illumination = object.illum_range()
                    elif device_name == "Red 3":
                        new_data.red_three_temperature = object.temp_range()
                        new_data.red_three_humidity = object.hum_range()
                        new_data.red_three_illumination = object.illum_range()
                    new_data.save()

        return JsonResponse({'response':'success'})
