from django.db import models
from django.contrib.auth.models import User

# Create your models here.
import uuid
from comments.models import Comment
from images.models import Image

# create contact us model

class EventImage(Image):
    pass

class EventComment(Comment):
    pass

class EventSchedule(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    repea_time = models.CharField(max_length=255, blank=True, null=True)
    by_day = models.DateTimeField()
    time_zone = models.TimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.repea_time


class EventType(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, blank=True, null=True)
    discription = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Event(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    event_type = models.ForeignKey(
        EventType, on_delete=models.CASCADE, related_name="event_type", null=True
    )
    name = models.CharField(max_length=255, blank=True, null=True)
    event_schedule = models.ForeignKey(
        EventSchedule, on_delete=models.CASCADE, related_name="event_schedule", null=True
    )
    discription = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    image = models.ManyToManyField(
        EventImage, related_name="event_images"
    )

    event_comments = models.ManyToManyField(
        EventComment, related_name="event_comments"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name



