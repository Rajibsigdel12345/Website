
from django.shortcuts import render
from django.views.generic import DetailView
from .models import Hotel
import time

# Create your views here.


class HotelRoom(DetailView):
    model = Hotel
