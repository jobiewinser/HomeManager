from django.urls import path
import plex.views as plexviews
urlpatterns = [
    path('/', plexviews.PlexView.as_view(), name='plex' ),   
    path('/plexwebhooks/', plexviews.PlexWebhookView.as_view(), name='plex_webhook_view' ),     
]