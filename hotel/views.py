from typing import Any, Dict
from django.forms.models import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import UpdateView, CreateView, View
from .models import Room, RoomBooking
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .forms import RoomForm
from hotelinfo.models import Hotel


# Create your views here.

def Booknow(request, pk):
    roominfo = Room.objects.get(pk=pk)
    Room.objects.filter(pk=pk).values().update(available=False)
    messages.success(
        request, f'Thank you {request.user} for booking room')  # Room no. {roominfo.getRoomnumber()} of {roominfo.hotel.name} has been booked by {request.user}
    hotel = roominfo.hotel.pk
    return redirect("hotelinfo:Room", hotel)


class RoomCreateView(LoginRequiredMixin, CreateView):
    model = Room
    login_url = reverse_lazy("home:Login")
    # success_url = reverse_lazy("hotelinfo:Room", args=[model.hotel])
    form_class = RoomForm

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        # form.instance.hotel = self.request.rooms.hotel
        id = self.kwargs.get('pk')
        form.instance.hotel = Hotel.objects.get(pk=id)
        return super().form_valid(form)

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        if self.form_valid:
            messages.success(request, "Room updated successfully")
        else:
            messages.error(request, "Invalid information")
        return super().post(request, *args, **kwargs)


class RoomUpdateView(UpdateView, LoginRequiredMixin):
    model = Room
    login_url = reverse_lazy("home:Login")
    form_class = RoomForm

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        if self.form_valid:
            messages.success(request, "Room updated successfully")
        else:
            messages.error(request, "Invalid information")
        return super().post(request, *args, **kwargs)

    # fields = ['room_number', 'room_style', 'booking_price', "available"]
    # success_url = reverse_lazy("home:homepage")
