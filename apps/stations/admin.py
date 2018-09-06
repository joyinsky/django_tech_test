from django.contrib import admin
from apps.stations.models import Location, Station

admin.site.register(Location)
admin.site.register(Station)
