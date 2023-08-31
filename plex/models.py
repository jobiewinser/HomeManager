from django.db import models
import home.models as home_models
import urllib
from django.core.files import File
import tempfile

class PlexAccount(home_models.BaseModel):
    model_identifier = "0005"
    plex_id = models.TextField(null=True, blank=True)
    title = models.TextField(null=True, blank=True)
    thumbnail_url = models.TextField(null=True, blank=True)
    thumbnail = models.ImageField(upload_to='media/plex_account_thumbnails/', null=True, blank=True)

    def save_thumbnail_from_url(self, url):
        if url:
            # Download the image from the URL
            response = urllib.request.urlopen(url)
            img_temp = tempfile.NamedTemporaryFile(delete=True)
            img_temp.write(response.read())
            img_temp.flush()

            # Save the image file in the model field
            self.image.save(f"image_{self.pk}.jpg", File(img_temp), save=True)
    
class PlexWebhook(home_models.Webhook):
    model_identifier = "0006"
    thumbnail_url = models.TextField(null=True, blank=True)
    thumbnail = models.ImageField(upload_to='media/plex_thumbnails/', null=True, blank=True)
    plex_account = models.ForeignKey('plex.PlexAccount', null=True, blank=True, on_delete=models.SET_NULL) 