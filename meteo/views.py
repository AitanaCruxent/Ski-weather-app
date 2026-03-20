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

    left_resorts = [r for r in resorts if r.top_lon < 1.5]
    right_resorts = [r for r in resorts if r.top_lon >= 1.5]

    # Sort LEFT → west to center (ascending)
    left_resorts.sort(key=lambda r: r.top_lon)

    # Sort RIGHT → east to center (descending)
    right_resorts.sort(key=lambda r: r.top_lon, reverse=True)

    return render(request, "meteo/skiresorts.html", {
        "resorts": resorts,
        "resorts_json": resorts_data,  # Pass the same data for JavaScript use
        "left_resorts": left_resorts,
        "right_resorts": right_resorts
    })