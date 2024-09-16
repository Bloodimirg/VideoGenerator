from django.urls import path
from .views import VideoViewSet

video_list = VideoViewSet.as_view({'get': 'video_generator'})

urlpatterns = [
    path('video-generate/', video_list, name='video-generate'),  # Здесь нет аргумента 'namespace'
]
