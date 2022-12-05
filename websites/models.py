from django.db import models

# Create your models here.
import uuid

# create contact us model
class ContactUs(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    full_name = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=254)
    company_name = models.CharField(max_length=150, blank=True, null=True)
    phone = models.CharField(max_length=150, unique=False)
    comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.company_name


class CourseInquries(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    course_name = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=254)
    company_name = models.CharField(max_length=150, blank=True, null=True)
    phone = models.CharField(max_length=150, unique=False)
    comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.company_name