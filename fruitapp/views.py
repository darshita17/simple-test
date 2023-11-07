from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, View

# Create your views here.
class HomeView(ListView):
    model = User
    template_name = "home.html"

def register(request):
    return render(request,'account/register.html')