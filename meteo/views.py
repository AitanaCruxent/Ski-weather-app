from django.http import HttpResponse
from django.shortcuts import render
from .models import Resort, Summit

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

def summits(request):
    summits = Summit.objects.all()
    summits_data = [
        {
            "id": s.id,
            "name": s.name,
            "lat": s.lat,
            "lon": s.lon,
            "top_elevation": s.top_elevation,
        }
        for s in summits
    ]

    left_summits = [s for s in summits if s.lon < 1.2]
    right_summits = [s for s in summits if s.lon >= 1.2]

    # Sort LEFT → west to center (ascending)
    left_summits.sort(key=lambda s: s.lon)

    # Sort RIGHT → east to center (descending)
    right_summits.sort(key=lambda s: s.lon)

    return render(request, "meteo/summits.html", {
        "summits": summits,
        "summits_json": summits_data,  # Pass the same data for JavaScript use
        "left_summits": left_summits,
        "right_summits": right_summits
    })