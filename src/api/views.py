# Create your views here.
from rest_framework import generics
from .models import Video
from .serializers import VideoSerializer

# Create your views here.
class VideoList(generics.ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer