from . import views
from django.urls import path
from django.shortcuts import redirect


app_name = "home"
urlpatterns = [
    path('', views.homeView.as_view(), name="homepage"),
    path('register/', views.SignupView.as_view(), name="Signup"),
    path('logout/', views.logout_request, name="Logout"),
    path('login/', views.Loginview.as_view(), name="Login")
]
