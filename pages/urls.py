from django.urls import path

from .views import HomePageDetailView

urlpatterns = [
    path('', HomePageDetailView.as_view(), name='home'),
]
