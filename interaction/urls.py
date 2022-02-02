from django.urls import path
from .views import LikeFlowerView
urlpatterns = [
    path('detail/<int:flower_id>/action/', LikeFlowerView.as_view(), name='like-flower'),
]