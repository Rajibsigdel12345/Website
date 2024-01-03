
from typing import Any
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .forms import NewUserForm, AuthenticationForm
from django.views.generic import View, ListView
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from hotelinfo.models import Account, Hotel

# Create your views here.


class homeView(ListView):
    model = Hotel
    template_name = "home\home.html"

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        print(request.GET)
        return super().get(request, *args, **kwargs)


class SignupView(CreateView):
    form_class = NewUserForm
    template_name = "home\signupform.html"

    def get(self, request, *args: str, **kwargs):
        if request.user.is_authenticated:
            messages.info(
                request, f"You are already logged in as {request.user}")
            return redirect("home:homepage")
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = NewUserForm(request.POST)
        if form.is_valid():
            # user = form.save(commit=False)
            if request.POST.get("username") not in User.objects.all():
                user = form.save()
                staff_test = request.POST.get("accountType")
                latest = User.objects.last().id
                t = User.objects.get(pk=latest)
                account = Account(username=t, actype=staff_test)
                account.save()
                if staff_test == 'RECEPTIONIST' or staff_test == 'HOUSEKEEPING':
                    x = User.objects.filter(pk=latest)
                    x.update(is_staff=True)

                login(request, user)
                messages.success(
                    request, f"{request.user} is  logged in as {account}")
                return redirect("home:homepage")
            else:
                messages.error(
                    request, "Unsuccessful registration. Invalid information.")
                return redirect("home:Signup")
        else:
            form = NewUserForm()
        return super().post(request, *args, **kwargs)


def logout_request(request):
    if request.user not in User.objects.all():
        messages.warning(request, "You were not logged in to beginwith")
        return redirect("home:homepage")
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect("home:homepage")


class Loginview(View):
    def get(self, request):
        print(request.GET.get('next'))
        form = AuthenticationForm(request)
        if (request.user.is_authenticated):
            messages.info(
                request, f"You are already logged in as {request.user}")
            return redirect("home:homepage")
        return render(request, "home\login.html", {"form": form})

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                account = Account.objects.get(username_id=user.pk)

                messages.success(
                    request, f"{username} is logged in successfully as {account} ")
                if request.GET.get('next'):
                    return redirect(request.GET.get('next'))
                else:
                    return redirect("home:homepage")
            else:
                messages.error(request, "Invalid username or password.")

        else:
            messages.error(request, "Invalid username or password.")
            return HttpResponseRedirect(self.request.get_full_path())
        form = AuthenticationForm()
        return redirect("home:homepage")
