from django.db import models
from django.contrib.auth.models import User

# Create your models here.
import uuid
from images.models import Image


class ClientsImage(Image):
    pass


class Clients(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, blank=True, null=True)
    disciption = models.TextField(blank=True, null=True)
    client_image = models.OneToOneField(ClientsImage, on_delete=models.CASCADE, related_name="client_image")
    address = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name or ""



