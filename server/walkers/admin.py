from django.contrib import admin
from .models import Walkers, ScheduledWalks, Schedules

admin.site.register(Walkers)
admin.site.register(ScheduledWalks)
admin.site.register(Schedules)
