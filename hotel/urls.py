from django.urls import path
from . import views

app_name = 'hotel'

urlpatterns = [
    path('<int:pk>/booknow/', views.Booknow, name="book"),
    path('<int:pk>/create/', views.RoomCreateView.as_view(), name="create"),
    path('<int:pk>/update/', views.RoomUpdateView.as_view(), name="update"),
]
