
from .models import Clients, ClientsImage
from rest_framework import serializers


class ClientsImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClientsImage
        fields = "__all__"

class ClientsSerializer(serializers.ModelSerializer):

    client_image = ClientsImageSerializer(many=False, required=False, allow_null=True)


    class Meta:
        model = Clients
        fields = ["id","name", "disciption", "client_image","address", "created_at", "updated_at",]
