from django.urls import path
import energy.views as energyviews
urlpatterns = [
    path('/', energyviews.EnergyView.as_view(), name='energy' ),     
]