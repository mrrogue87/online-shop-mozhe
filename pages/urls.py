from django.urls import path

from .views import HomePageDetailView,CategoryListView

urlpatterns = [
    path('', HomePageDetailView.as_view(), name='home'),
    path('<int:pk>/', CategoryListView.as_view(), name='category_list'),
]
