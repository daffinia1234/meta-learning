from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about),
    path('menu/',views.menu),
    path('postproperty/',views.NewProperty),
]