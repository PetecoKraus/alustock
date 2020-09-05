from django.contrib import admin

from .models import Profile, Treatment, Extruder, ProductSystem

class TreatmentAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,            {'fields': ['color_name']}),
        ('Color Preview', {'fields': ['preview']}),
    ]

admin.site.register(Profile)
admin.site.register(Treatment)
admin.site.register(Extruder)
admin.site.register(ProductSystem)