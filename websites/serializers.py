import websites.models as models
from rest_framework import serializers


# contact serializer class
class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ContactUs
        fields = "__all__"