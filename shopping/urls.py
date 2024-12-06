from django.urls import path
from shopping.views import *

app_name="grocery"

urlpatterns=[
    path('grocery/',grocery,name='grocery'),
]