from django.shortcuts import render
import home.views as home_views
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.shortcuts import HttpResponse


# Create your views here. 
@method_decorator(csrf_exempt, name='dispatch')
class PlexWebhookView(home_views.BaseWebhookView):
    def post(self, request): 
        webhook_instance = self.create_webhook_instance(request)
        return HttpResponse( "text", 200)