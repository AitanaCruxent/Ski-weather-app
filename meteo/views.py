from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.utils import timezone
from datetime import timedelta


from .models import User, Resort, Summit, Route


def index(request):

    one_week_ago = timezone.now() - timedelta(days=7)

    routes = Route.objects.filter(timestamp__gte=one_week_ago).order_by("-date_completed")

    return render(request, "meteo/index.html", {
        "routes": routes
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "meteo/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "meteo/login.html")
    
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "meteo/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save() 
        except IntegrityError:
            return render(request, "meteo/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "meteo/register.html")
       
@login_required
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

@login_required
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

@login_required
def bpa(request):
    return render(request, "meteo/bpa.html")

@login_required
def myroutes(request):
    routes = Route.objects.filter(owner=request.user).order_by("-date_completed", "-timestamp")

    return render(request, "meteo/myroutes.html", {
        "routes": routes,
        "locations": Route.LOCATION_CHOICES
    })

@login_required
def addroute(request):

    if request.method == "POST":
        name = request.POST.get("name")
        location = request.POST.get("location") or "Pirineus"
        weather_info = request.POST.get("weather_info") or ""
        distance_km = request.POST.get("distance_km") or None
        duration_hours = request.POST.get("duration_hours") or None
        duration_minutes = request.POST.get("duration_minutes") or None
        date_completed = request.POST.get("date_completed")

        required_fields = {
            "name": name,
            "location": location,
            "date": date_completed,
        }

        if not all(required_fields.values()):
            messages.error(request, "Please complete all required fields name, location and date.")
            return redirect("myroutes")
    
        new_route = Route(
            owner = request.user,
            name = name,
            location = location,
            weather_info = weather_info,
            distance_km = distance_km,
            duration_hours = duration_hours,
            duration_minutes = duration_minutes,
            date_completed = date_completed
        )

        new_route.save()
        messages.success(request, "Your route was saved successfully")
        return redirect("myroutes")

    else:
        location = Route.LOCATION_CHOICES
        return render(request, "meteo/myroutes.html", {
            "location": location
        })

@login_required
@require_POST
def deleteroute(request, route_id):
    route = get_object_or_404(
        Route,
        id=route_id,
        owner=request.user
    )

    route.delete()

    messages.success(request, "Route deleted successfully.")
    return redirect("myroutes")
