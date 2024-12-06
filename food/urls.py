from django.urls import path
from food.views import *

app_name="eating"

urlpatterns=[
    path('nonveg/',nonveg,name='nonveg'),
]