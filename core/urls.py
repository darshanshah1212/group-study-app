from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path("room/<str:room_name>/",views.index,name="index")
]
