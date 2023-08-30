from datetime import datetime
from django.db import models
import uuid
class BaseModel(models.Model):
    model_identifier = "0000"
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    guid = models.TextField(null=True, blank=True)
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.created:
            self.created = datetime.now() 
        if not self.guid:
            self.guid = f"{self.model_identifier}-{str(uuid.uuid4())[:16]}"
        self.updated =  datetime.now()
        super(BaseModel, self).save(force_insert, force_update, using, update_fields)

class Webhook(BaseModel):
    model_identifier = "0001"
    headers = models.JSONField(default=dict)
    json_data = models.JSONField(default=dict)
    meta_data = models.JSONField(default=dict)
    user_agent = models.TextField(null=True, blank=True)
    url = models.TextField(null=True, blank=True)  
    
class Device(BaseModel):
    model_identifier = "0002"
    alias = models.TextField(null=True, blank=True)
    device_id = models.TextField(null=True, blank=True)
    device_type = models.TextField(null=True, blank=True)
    host = models.TextField(null=True, blank=True)
    mac = models.TextField(null=True, blank=True)
    model = models.TextField(null=True, blank=True)
    