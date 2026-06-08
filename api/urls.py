from django.urls import path
from .views import hello, current_time

urlpatterns = [
    path("hello/", hello),
    path("time/", current_time),
]