from django.contrib import admin
import home.models as home_models
# Register your models here.


class WebhookAdmin(admin.ModelAdmin):
    list_display = ['created', 'updated', 'user_agent']
    search_fields = ['created', 'updated', 'user_agent']
admin.site.register(home_models.Webhook, WebhookAdmin)