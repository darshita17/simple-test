from django.urls import include,path
from .views import (HomeView,register)
from fruitapp import views

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('register/',views.register,name='register')
]
