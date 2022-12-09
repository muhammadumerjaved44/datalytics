
from .models import Event, EventType, EventImage, EventComment
from rest_framework import serializers


class EventImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = EventImage
        fields = "__all__"

class EventCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = EventComment
        fields = "__all__"


class EventTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = EventType
        fields = "__all__"


class EventSerializer(serializers.ModelSerializer):

    event_type = EventTypeSerializer(many=False, required=False, allow_null=True)
    event_images = EventImageSerializer(many=True, required=False, allow_null=True)
    event_comments = EventCommentSerializer(many=True)


    class Meta:
        model = Event
        fields = ["id","event_type","name","start_date","end_date","repea_time","by_day","time_zone","discription","location","created_at","updated_at","event_images", "event_comments"
        ]
        # fileds = "__all__"
