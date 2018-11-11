from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^videos/$', views.VideoList.as_view(), name='video-list'),
]