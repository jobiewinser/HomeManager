from django.db import models
import home.models as home_models
# Create your models here.

     
class KasaDevice(home_models.Device):
    model_identifier = "0003"
    on_since = models.DateTimeField(null=True, blank=True)
    is_bulb = models.BooleanField(null=False, default = False)
    is_color = models.BooleanField(null=False, default = False)
    is_dimmable = models.BooleanField(null=False, default = False)
    is_dimmer = models.BooleanField(null=False, default = False)
    is_light_strip = models.BooleanField(null=False, default = False)
    is_off = models.BooleanField(null=False, default = False)
    is_on = models.BooleanField(null=False, default = False)
    is_plug = models.BooleanField(null=False, default = False)
    is_strip = models.BooleanField(null=False, default = False)
    is_strip_socket = models.BooleanField(null=False, default = False)
    is_variable_color_temp = models.BooleanField(null=False, default = False)
    has_emeter = models.BooleanField(null=False, default = False)
    led = models.BooleanField(null=False, default = False)
    def latest_meter_reading(self):
        return self.meterreading_set.last()
class MeterReading(home_models.BaseModel):
    model_identifier = "0004"
    realtime_current_reading = models.FloatField(null=False, default = 0.0) 
    realtime_power_reading = models.FloatField(null=False, default = 0.0) 
    realtime_total_reading = models.FloatField(null=False, default = 0.0) 
    realtime_voltage_reading = models.FloatField(null=False, default = 0.0) 
    day_reading = models.FloatField(null=False, default = 0.0) 
    month_reading = models.FloatField(null=False, default = 0.0) 
    kasa_device = models.ForeignKey('energy.KasaDevice', null=True, blank=True, on_delete=models.CASCADE) 