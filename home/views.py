from django.shortcuts import render
from django.views.generic import TemplateView, View
import home.models as home_models  
import json 
class HomeView(TemplateView):
    template_name = "home/homeview.html"
    
    def get(self, request, **kwargs):            
        return super(HomeView, self).get(request, **kwargs)
    
class BaseWebhookView(View):
    def create_webhook_instance(self, request):
        headers = dict(request.headers) # dict, e.g {"user-agent": "Ombi/4.39.1 (https://ombi.io/)"...}  
        user_agent = headers.get("User-Agent")
        url = request._current_scheme_host + request.path
        json_data = json.loads(request.body)
        home_models.Webhook.objects.create(
            headers = headers,
            json_data = json_data,
            user_agent = user_agent,
            url = url,
        ) 