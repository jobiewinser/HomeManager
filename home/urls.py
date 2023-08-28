from django.urls import path
import home.views as homeviews
urlpatterns = [
    path('/', homeviews.HomeView.as_view(), name='home' ),     
]