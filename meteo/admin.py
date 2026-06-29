from django.contrib import admin
from .models import User, Resort, Summit

admin.site.register(User)
admin.site.register(Resort)
admin.site.register(Summit)