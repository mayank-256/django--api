from django.http import JsonResponse
from datetime import datetime

def hello(request):
    return JsonResponse({
        "message": "Hello World"
    })

def current_time(request):
    return JsonResponse({
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })