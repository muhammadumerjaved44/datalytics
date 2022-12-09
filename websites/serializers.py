import websites.models as models
import courses.models as courses_models
import events.models as events_models
from rest_framework import serializers


# contact serializer class
class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ContactUs
        fields = "__all__"


# class HomeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = courses_models.Course
#         fields = "__all__"
