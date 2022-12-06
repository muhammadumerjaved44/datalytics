from django.db import models
from django.contrib.auth.models import User

# Create your models here.
import uuid
from comments.models import Comment
from images.models import Image

# create contact us model

class CourseCategory(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, blank=True, null=True)
    discription = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name or ""

class CourseCategoryImage(Image):
    course_catagoery = models.ForeignKey(CourseCategory, on_delete=models.CASCADE, related_name="course_catagoery_image")


class CourseInstructure(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="user", null=True
    )
    # course = models.ForeignKey(Course, related_name="course", on_delete=models.CASCADE)
    discription = models.TextField(blank=True, null=True)
    job_title = models.CharField(max_length=255, blank=True, null=True)
    facebook_link = models.CharField(max_length=255, blank=True, null=True)
    linkedin_link = models.CharField(max_length=255, blank=True, null=True)
    instagram_link = models.CharField(max_length=255, blank=True, null=True)
    twitter_link = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email or ""

class InstructureImage(Image):
   course_instructure = models.ForeignKey(CourseInstructure, on_delete=models.CASCADE, related_name="course_instructure_image")

class Course(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    course_catagoery = models.ForeignKey(
        CourseCategory, on_delete=models.CASCADE, related_name="course_catagoery"
    )
    course_instructure = models.ForeignKey(CourseInstructure, related_name="course_instructure", on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True, null=True)
    course_code = models.CharField(max_length=255, blank=True, null=True)
    course_mode = models.CharField(max_length=255, blank=True, null=True)
    discription = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name or ""


class CourseComments(Comment):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="course_comment")
class CourseImage(Image):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="course_image")
