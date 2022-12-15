from django.db import models
from django.contrib.auth.models import User

# Create your models here.
import uuid
from comments.models import Comment
from images.models import Image
import pytz
from pytz import country_names, country_timezones
ALL_TIME_ZONE = [('--', 'Please select the timezone')]
ALL_TIME_ZONE.extend([(v,v) for i, v in enumerate(pytz.all_timezones)])

class EventType(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, blank=True, null=True)
    discription = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name or ""

class Event(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    event_type = models.ForeignKey(
        EventType, on_delete=models.CASCADE, related_name="event_type"
    )
    name = models.CharField(max_length=255, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    start_time = models.TimeField(blank=True, null=True)
    end_date = models.DateField()
    end_time = models.TimeField(blank=True, null=True)

    time_zone = models.CharField(
        max_length=100,
        choices=ALL_TIME_ZONE,
        default="Asia/Karachi",
    )
    discription = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    is_upcomming = models.BooleanField(default=False)
    is_done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name or ""

class EventImage(Image):
    event_images = models.ForeignKey(
        Event, related_name="event_images", on_delete=models.CASCADE
    )

class EventComment(Comment):
    event_comments = models.ForeignKey(
        Event, related_name="event_comments", on_delete=models.CASCADE
    )

