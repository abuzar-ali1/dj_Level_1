from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from .models import Profile , HackathonIdea
# Create your views here.

def welcome(request):
    return HttpResponse("<h1>Welcome in the Django Project</h1>")


def get_all_profiles(request):
    profile_list = list(Profile.objects.values())
    return JsonResponse({ "Profiles" : profile_list})


def get_all_hacks(request):
    Hackthons  = list(HackathonIdea.objects.values())
    return JsonResponse({ 'Hackothons' :Hackthons})


def filtererd_data(request):
    data = list(HackathonIdea.objects.filter(is_free_entry = True).values())
    return JsonResponse({'data' : data})


def id_base_data(request):
    query =  request.GET.get('id')
    result  = list(HackathonIdea.objects.get('{query}').values())
    if query:
        return JsonResponse({'data' : result})
    else:

        message = "You did not provide a search query."
