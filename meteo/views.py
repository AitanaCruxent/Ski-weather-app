from django.http import HttpResponse
from django.shortcuts import render
from .models import Resort

# Create your views here.

def index(request):
    return render(request, "meteo/index.html")

def skiresorts(request):
    resorts = Resort.objects.all()
    resorts_data = [
        {
            "id": r.id,
            "name": r.name,
            "base_lat": r.base_lat,
            "base_lon": r.base_lon,
            "top_lat": r.top_lat,
            "top_lon": r.top_lon,
            "base_elevation": r.base_elevation,
            "top_elevation": r.top_elevation,
        }
        for r in resorts
    ]
    return render(request, "meteo/skiresorts.html", {
        "resorts": resorts,
        "resorts_json": resorts_data,  # Pass the same data for JavaScript use
    })