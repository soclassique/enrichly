from django.urls import path
#from .views import home,index,SignUp
from .import views

urlpatterns = [
#path('', home, name = "home"),
#path('', index, name = "index"),
path('', views.home, name = "home"),
path("signup/", views.SignUp.as_view(), name="signup"),
]