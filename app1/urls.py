from django.urls import path
from . import views


urlpatterns = [
    path('home/' , views.home , {"message" : "THis is the HOme page and THis is comming form the passing the data to the Url"}),
    path('api/greeting/<username>/' , views.greeting)
]
