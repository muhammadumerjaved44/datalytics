from django.db import models
from polymorphic.models import PolymorphicModel

# Create your models here.
import uuid
from django.conf import settings

# create contact us model




class Image(PolymorphicModel):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to="image_files/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.id



