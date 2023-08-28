from django.urls import path
import plex.views as plexviews
urlpatterns = [
    path('/plexwebhooks/', plexviews.PlexWebhookView.as_view(), name='plex_webhook_view' ),     
]