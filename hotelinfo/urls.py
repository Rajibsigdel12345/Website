from django.urls import path
from . import views

app_name = "hotelinfo"
urlpatterns = [
    path('<int:pk>/', views.HotelRoom.as_view(), name="Room"),
]
