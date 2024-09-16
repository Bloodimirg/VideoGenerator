from django.urls import path
from .views import VideoViewSet, HomePageView

video_list = VideoViewSet.as_view({'get': 'video_generator'})

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('video-generate/', video_list, name='video-generate'),
]
