from django.shortcuts import render

# Create your views here.

def home_view(request):
    return render(request, "pages/home.html")

def group_view(request):
    return render(request, "pages/groups.html")

def event_view(request):
    return render(request, "pages/events.html")