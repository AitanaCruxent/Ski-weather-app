from django.contrib import admin
from .models import User, Resort, Summit, Route

admin.site.register(User)
admin.site.register(Resort)
admin.site.register(Summit)
admin.site.register(Route)