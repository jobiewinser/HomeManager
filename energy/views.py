from django.shortcuts import render
from django.views.generic import TemplateView, View
import home.models as home_models  
import energy.models as energy_models  
import json 
import datetime
import asyncio
from kasa.discover import Discover
class EnergyView(TemplateView):
    template_name = "energy/energyview.html"
    
    def get(self, request, **kwargs):
        # get_kasa_devices()
        return super(EnergyView, self).get(request, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super(EnergyView, self).get_context_data(**kwargs)
        context['kasa_devices'] = energy_models.KasaDevice.objects.all()
        return context
    
def get_kasa_devices():    
    found_devices = asyncio.run(Discover.discover())
    for device_ip, device in found_devices.items():
        kasa_device_instance, created = energy_models.KasaDevice.objects.get_or_create(device_id=device.device_id) 
        kasa_device_instance.alias = device.alias
        kasa_device_instance.device_type = device.device_type.name
        kasa_device_instance.host = device.host
        kasa_device_instance.mac = device.mac
        kasa_device_instance.model = device.model 
        kasa_device_instance.on_since = device.on_since
        kasa_device_instance.is_bulb = device.is_bulb
        kasa_device_instance.is_color = device.is_color
        kasa_device_instance.is_dimmable = device.is_dimmable
        kasa_device_instance.is_dimmer = device.is_dimmer
        kasa_device_instance.is_light_strip = device.is_light_strip
        kasa_device_instance.is_off = device.is_off
        kasa_device_instance.is_on = device.is_on
        kasa_device_instance.is_plug = device.is_plug
        kasa_device_instance.is_strip = device.is_strip
        kasa_device_instance.is_strip_socket = device.is_strip_socket
        kasa_device_instance.is_variable_color_temp = device.is_variable_color_temp
        kasa_device_instance.has_emeter = device.emeter_type == 'emeter'
        kasa_device_instance.led = device.led
        kasa_device_instance.save()
        
        if device.has_emeter: 
            asyncio.run(device.update())
            now = datetime.datetime.now() 
            meter_reading_instance, created = energy_models.MeterReading.objects.get_or_create(kasa_device=kasa_device_instance, created=now) 
            meter_reading_instance.realtime_current_reading = device.emeter_realtime.current
            meter_reading_instance.realtime_power_reading = device.emeter_realtime.power
            meter_reading_instance.realtime_total_reading = device.emeter_realtime.total
            meter_reading_instance.realtime_voltage_reading = device.emeter_realtime.voltage
            meter_reading_instance.day_reading = device.emeter_today
            meter_reading_instance.month_reading = device.emeter_this_month
            meter_reading_instance.save() 
            