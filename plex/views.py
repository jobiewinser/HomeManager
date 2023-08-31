from django.shortcuts import render
from django.views.generic import TemplateView, View
import home.views as home_views
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.shortcuts import HttpResponse
import plex.models as plex_models
import json

class PlexView(TemplateView):
    template_name = "plex/plexview.html"
    
    def get(self, request, **kwargs): 
        return super(PlexView, self).get(request, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super(PlexView, self).get_context_data(**kwargs)
        context['plex_accounts'] = plex_models.PlexAccount.objects.all().order_by("pk")
        context['plex_webhooks'] = plex_models.PlexWebhook.objects.all().order_by("-pk")
        return context
    
    
    
# Create your views here. 
@method_decorator(csrf_exempt, name='dispatch')
class PlexWebhookView(home_views.BaseWebhookView):
    def post(self, request): 
        plex_webhook_instance = self.create_plex_webhook_instance(request)
        print(plex_webhook_instance)
        return HttpResponse( "text", 200)
    
    def create_plex_webhook_instance(self, request):
        headers = dict(request.headers) 
        user_agent = headers.get("User-Agent")
        url = request._current_scheme_host + request.path
        json_data = {}
        if request.FILES:
            payload = request.FILES.get('payload')
            if payload: 
                contents = payload.read()
                decoded_contents = contents.decode('utf-8')
                json_data = json.loads(decoded_contents)  
        plex_account_json = json_data.get('Account', {})
        plex_account_instance, plex_account_created = plex_models.PlexAccount.objects.get_or_create(
            plex_id = plex_account_json.get('id')
        )
        thumb = plex_account_json.get('thumb')
        if plex_account_created or thumb != plex_account_instance.thumbnail_url:
            plex_account_instance.save_thumbnail_from_url(thumb)
        plex_account_instance.thumbnail_url = thumb
        plex_account_instance.title = plex_account_json.get('title')
        plex_account_instance.save()
        
        plex_webhook_instance = plex_models.PlexWebhook.objects.create(
            headers = headers,
            json_data = json_data,
            user_agent = user_agent,
            url = url,
            plex_account = plex_account_instance
        ) 
        return plex_webhook_instance