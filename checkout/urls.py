from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
    path('make_order' ,views.make_order,name='make_order' ),
]
