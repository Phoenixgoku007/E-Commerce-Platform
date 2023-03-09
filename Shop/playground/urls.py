from django.urls import path
from .import views

urlpatterns = [
    path('', views.say_hello) # always end the route with / inside the quotation. If i don't mention any route it directly gets opened on main page oterwise it will open on specified path.
]

