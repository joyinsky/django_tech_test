from django.contrib import admin
from apps.lines.models import Line, Route
# Register your models here.

admin.site.register(Line)
admin.site.register(Route)
