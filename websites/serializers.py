from .models import Contact
from rest_framework import serializers


# contact serializer class
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"