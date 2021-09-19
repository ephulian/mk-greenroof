
from django.views.generic import View
from django.http import JsonResponse

class SensorDateview(View):
    def get(self, request):
        return JsonResponse({'response':'success'})

    def post(self, request):
        return JsonResponse({'response':'success'})
