from django.urls import path
from .views import home #,SignUp

urlpatterns = [
path('', home, name = "home"),
]