from django.urls import path
from Test.views import viewform

urlpatterns=[
    path('property/',viewform,name="property"),
]