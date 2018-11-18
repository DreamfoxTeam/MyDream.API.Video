# Create your views here.
from rest_framework import generics
from rest_framework import filters
from .models import Video
from .serializers import VideoSerializer


# Create your views here.
class VideoList(generics.ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    filter_backends = (filters.SearchFilter,filters.OrderingFilter,)
    search_fields = ('id', 'title')
    ordering_fields = '__all__'
    