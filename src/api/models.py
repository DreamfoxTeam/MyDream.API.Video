from django.db import models
from datetime import datetime  

# Create your models here.
class Video(models.Model):
    class Meta:
        db_table = 'video'
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    seconds = models.IntegerField()
    created = models.DateTimeField(blank=True)
    def __str__(self):
        return self.title