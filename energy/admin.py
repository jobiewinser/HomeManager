from django.contrib import admin
import energy.models as energy_models
# Register your models here.


class KasaDeviceAdmin(admin.ModelAdmin):
    list_display = ['alias']
    search_fields = ['alias']
admin.site.register(energy_models.KasaDevice, KasaDeviceAdmin)

class MeterReadingAdmin(admin.ModelAdmin):
    list_display = ['created']
    search_fields = ['created']
admin.site.register(energy_models.MeterReading, MeterReadingAdmin)