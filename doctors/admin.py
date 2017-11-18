from django.contrib import admin

# Register your models here.
from doctors.models import *


class AppoitAdmin(admin.StackedInline):
    model = Time
    extra = 5


class Appoitment(admin.ModelAdmin):
    inlines = [AppoitAdmin]


class TimerAdmin(admin.StackedInline):
    model = ExtraTime
    extra = 10


class Timer(admin.ModelAdmin):
    inlines = [TimerAdmin]


admin.site.register(Time, Timer)
admin.site.register(Doctor, Appoitment)
admin.site.register(Schedule)
