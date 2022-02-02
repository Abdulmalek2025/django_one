from unicodedata import name
from django.urls import path
from .views import HomeView,FlowerDetailView
urlpatterns = [
    path('',HomeView.as_view(), name='home'),
    path('detail/<int:pk>/', FlowerDetailView.as_view(), name='flower-detail'),
]