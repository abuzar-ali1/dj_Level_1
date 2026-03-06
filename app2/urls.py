from django.urls import path
from app2.views import get_all_profiles , welcome , get_all_hacks

urlpatterns = [
    path('api/profiles/', get_all_profiles),
    path('' , welcome),
    path('api/ideas/' , get_all_hacks)
    # ... your other urls
]