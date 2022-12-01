from django.db import models

# Create your models here.
import uuid

# create contact us model
class Contact(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    full_name = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=254)
    company_name = models.CharField(max_length=150, blank=True, null=True)
    phone = models.CharField(max_length=150, unique=False)
    comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.company_name



# class SectionType(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     section_name = models.CharField(max_length=20)
#     title = models.CharField(max_length=255, blank=True, null=True)
#     image = models.ImageField(null=True, blank=True, upload_to="icon")
#     description = models.TextField(blank=True, null=True)

#     def __str__(self):
#         return self.section_name



# # create Section us model
# class Section(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     section_type = models.ForeignKey(
#         SectionType, on_delete=models.CASCADE, related_name="section", null=True
#     )
#     image = models.ImageField(null=True, blank=True, upload_to="icon")
#     title = models.CharField(max_length=20)
#     description = models.TextField(blank=True, null=True)
#     class_icon = models.CharField(max_length=50, null=True, blank=True)
#     seo_meta_tags = models.TextField(blank=True, null=True)
#     is_visible = models.BooleanField(default=False)

#     def __str__(self):
#         return self.title