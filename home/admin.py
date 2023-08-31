from django.contrib import admin
import home.models as home_models
from django.apps import apps
# Register your models here.


class WebhookAdmin(admin.ModelAdmin):
    list_display = ['created', 'updated', 'user_agent']
    search_fields = ['created', 'updated', 'user_agent']
admin.site.register(home_models.Webhook, WebhookAdmin)



all_models = apps.get_models()

# Register all non-specified models
for model in all_models:
    if not admin.site.is_registered(model):
        admin.site.register(model)